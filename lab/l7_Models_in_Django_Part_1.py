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


6. Admin

dobavqneto na pyrviq potrebitel stava s komanda
    python manage.py createsuperuser

daniel, daniel_zorov@abv.bg, Maimun06
http://127.0.0.1:8000/admin/


7. In admin.py:

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    pass

Now this model is enabled in django admin
You can edit data in the Employees table from admin

* Ako napravim __str__ v Employess modela, toi se pokazva pri spisyka na employees v admin


8. * You can reverse a migration


9. * Additional configuration of fields

    field = models............(
        unique = True,          # vsichki zapisi v kolonata sa unikalni
        default = 1,
        null = True             # empty values will be stored as null, False by default
        blank = True,           # if true the field is allowed to be blank, False by default
        primary_key = True,

        choices = (
            ('jr', 'Junior'),       # pyrvoto se zapisva a vtoroto se pokazva kato izbirash
            ('reg', 'Regular'),
        ),

        verbose_name = 'Seniority level',   # izpisva se vmesto 'field' v admin

        editable = False,
    )


10. Relationship one-to-many

    first create another table and migrate

    then in the first table(class) make the connection and migrate:

        department = models.ForeignKey(
            Department,                     # kym koq dr tablica sochi
            on_delete=models.CASCADE,       # kato iztriem department iztriva employee-to
        )

    * on_delete=models.SET_NULL, null=True
    * on_delete=models.RESTRICT        # ne mojesh da iztriesh department ako neshto e zakacheno kym nego


11. Relationship many-to-many

    project = models.ManyToManyField(Project)

    syzdava i mejninna tablica avtomatichno


12. One-to-One

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


13. Custom Django Admin Site

in:

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    pass

we can add:

    list_display = ('pk', 'fist_name', 'last_name', 'level')    # pokazva spisyk
    list_filter = ('level',)                                    # list filter
    search_fields = ('fist_name', 'last_name')                  # search

    fieldsets = (                                               # podrejda gi v sekcii
        (
            'Personal Info',
            {
                'fields': ('first_name', 'last_name'),
            }
        )
    ),

moje i custom neshta kato metodi:

    def department(self, obj):
        return obj.department.name


















"""
