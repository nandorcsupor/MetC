# Requirements
To install the required packages, run:
`pip install -r requirements.txt`

## POSTGRES

# Modify settings.py 'DATABASES' with your local credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'metdb',
        'USER': 'postgres', 
        'PASSWORD': 'postgres',
        'HOST': 'localhost', # 127.0.0.1
        'PORT': '5432',
    }
}

# Create Database
- Log in to your local postgres
    `sudo -u postgres psql`

- Create database
    `CREATE DATABASE metdb;`

# Run Migrations
`python manage.py makemigrations`
`python manage.py migrate`

# Run server
`python manage.py runserver`

# Test Test
`python manage.py test`

