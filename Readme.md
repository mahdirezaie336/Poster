# Poster - An ad registration service

## Back-End A

We used django as the backend for this service. The backend is a REST API that is used by the frontend to register ads and get the ads.

## Installation

First things first, install the requirements:

```bash
pip install -r requirements.txt
```

You need 3 things to run this backend:

1. A MySQL database.
2. An amazon S3 bucket.
3. A rabbitmq server

Go to `backend/Poster/` and create a file `secret.py`:

```bash
cd backend/Poster/
nano secret.py
```

Add the following variables with values of your database and s3 service info:

```python
AWS_S3_SECRET_ACCESS_KEY = None
AWS_S3_REGION_NAME = None
AWS_S3_ENDPOINT_URL = None
AWS_S3_ACCESS_KEY_ID = None
AWS_STORAGE_BUCKET_NAME = None
DB_NAME, DB_USER = None
DB_PASSWORD = None
DB_HOST = None
DB_PORT = None
```

Then go to `backend/api/` and add a file `secret.py`:

```bash
cd backend/api/
nano secret.py
```

Add the following variable with url of your rabbitmq service:

```python
AMQP_URL = None
```

### Back-End A Usage

To run this project simply run the following command:

```bash
cd backend
python manage.py runserver
```

Then open your browser and go to `http://localhost:8000/` to see the project.

## Back-End B

This service gets data from rabbitmq queue and sends it to image processing service. Then sends a verification email using MailGun service.

### Installation

Just go to `backend-b/` folder and create a file `secret.py`:

```bash
cd backend-b/
nano secret.py
```

Then add the following line:

```python
MAIL_GUN_DOMAIN = None
MAIL_GUN_API_KEY = None

DB_NAME = None
DB_USER = None
DB_PASSWORD = None
DB_HOST = None
DB_PORT = None

API_AUTH = 'Basic' + <Your imagga token> # This is authentication part of Imagga service

AMQP_URL = None
```

### Run Back-End B

Simply go the directory and run main.py file.

```bash
cd backend-b
python3 main.py
```
