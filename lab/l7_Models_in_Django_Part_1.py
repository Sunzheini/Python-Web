# Models in Django - Part 1


# After step6 in l6
"""

1. In models.py:

class Employees(models.Model):
    pass

sled syzdavaneto na tozi klas (dori samo s pass) veche ne se nalaga da pishem sql
Django ORM - Odject Relational Mapping - python koda se prevejda do sql
vseki klas (model) se svyrzva s 1 tablica ot db


some methods:
    Employees.objects.all()     # SQL: Select
    Employees.objects.create()  # SQL: Insert
    Employees.objects.filter()  # SQL Select + Where
    Employees.objects.update()  # SQL Update

    Employees.objects.raw('SELECT *')   # we can use raw SQL if we want


2. Paste this in settings.py to log raw SQL

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}


3. Create fields (columns in the db table)

1 class attribute == 1 column
fields cannot have more than 1 underscore and end with an underscore:

    class Employees(models.Model):
        first_name = models.CharField(
            max_length=30,
        )

Types:

    id is created by default
    CharField == Varchar(30): string with max length 30
    TextField == strings with unlimited length
    IntegerField == integers
    PositiveIntegerField == integers > 0
    FloatField == floats
    created_on = models.DateTimeField(
        auto_now=True,          # when we create the object
        auto_now_add=True,      # when we change the data of the object
    )
    BooleanField
    EmailField - naslqdqna charfield i dobavq validacii


4. Models migration

in the beginning or after a change
    python manage.py makemigrations     # create a migrations file
    python manage.py migrate            # apply migrations


5. Postgres

Replace in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employees_db',         # should be the same name as the DB created below
        'USER': 'postgres-user',
        'PASSWORD': 'password',
        'HOST': 'localhost',    # Not host.docker.internal - only for pgadmin
        'PORT': '5432',
    }
}

Database --> + --> Data Source --> PostresSql
--> User: postgres-user, Pass: password --> Test Connection --> Ok

Rightclick on postgres@localhost --> New --> Database --> Name it --> Ok

pip install psycopg2

python manage.py migrate

Database --> Refresh

Click on "1 of 3" next to employees_db and select default schema


6. -2:21:25 (1:46:11)










"""
