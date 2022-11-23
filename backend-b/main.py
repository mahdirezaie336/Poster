from rabbitmq import RabbitMQ
from secret import *
import json
import requests
import base64
import pandas as pd
import mysql.connector as mysql


queue = RabbitMQ()
TAGGER_ENDPOINT = 'https://api.imagga.com/v2/tags'

print("Creating database objects....")
mydb = mysql.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
my_cursor = mydb.cursor()
print("Connected to the database.")


def send_email(email, category, is_vehicle):
    body = f"Your post was {'' if is_vehicle else 'not'} approved! {'Category: ' + category if is_vehicle else ''}"
    requests.post(
        f"https://api.mailgun.net/v3/{MAIL_GUN_DOMAIN}/messages",
        auth=("api", MAIL_GUN_API_KEY),
        data={"from": f"Excited User <mailgun@{MAIL_GUN_DOMAIN}>",
              "to": [email],
              "subject": "Your post on the site",
              "text": body})


def callback(ch, method, properties, body):
    print("Received message # %r" % body)

    # get data from message
    data = json.loads(body)
    image_url = data['image']
    post_id = data['id']
    email = data['email']

    # Download the image
    image_server_response = requests.get(image_url)

    # If there is problem loading image url
    if image_server_response.status_code != 200:
        print('Error getting image from url')
        return

    # Get image data and convert to base 64
    image = image_server_response.content
    image_base64 = base64.b64encode(image).decode('utf-8')

    # Post image to the API
    headers = {
        'Authorization': API_AUTH,
    }
    tag_response = requests.post(TAGGER_ENDPOINT, data={'image_base64': image_base64}, headers=headers)

    # If there is problem with the API
    if tag_response.status_code != 200:
        print('Error getting tags from API')
        return

    # Get the tags
    tag_response_json = tag_response.json()['result']['tags']
    df = pd.DataFrame(tag_response_json)
    df.tag = df.tag.apply(lambda x: x['en'])

    # Get tags with confidence > 50
    df = df[df.confidence > 50]

    # Find tags containing 'vehicle'
    is_vehicle = not df[df.tag.str.lower().str.contains('vehicle')].empty

    if is_vehicle:
        print('Vehicle detected')
        # Query to mysql to change post status to 'APPROVED'
        query = f"UPDATE posts_post SET state = 'A', category = 'vehicle' WHERE id = {post_id}"
    else:
        print('No vehicle detected')
        # Query to mysql to change post status to 'REJECTED'
        query = f"UPDATE posts_post SET state = 'R' WHERE id = {post_id}"

    # Update post state and category
    my_cursor.execute(query)
    mydb.commit()
    print('Post status updated!')

    # Send email to user
    # send_email(email, 'vehicle', is_vehicle)
    print('Email sent to user', email)


def main():
    print("Starting to receive messages...")
    try:
        queue.start_receiving(callback)
    finally:
        queue.close()
        mydb.close()
    print("Finished receiving messages.")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
