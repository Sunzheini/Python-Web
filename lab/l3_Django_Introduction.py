# Django Introduction


# Framework e next-level biblioteka
"""
MV*

- Model contains the data (Database)
- View handles the UI
- * handles business logic, gets / sets data into model, return data to view


Django izpolzva MTV
- Model: kato gorniq model
- Template: kato gornoto view
- View: kato gornata *
"""

# Migraciqta ot python class generira SQL zaqvki, koito da se izpylnqt ot database
# APP oznachava chast ot nashiq dait, koqto e nezavisima ot ostanalite
# vseki APP si ima MTV i moje da se sydyrja v nqkolko proekta

# porta 8000 moje da go promenim
# ako sa nqkolko proekta da smenqm porta (ako a pusnati nqkolko)
# runserver e edinstevo za development celi!

# -------------------------------------------------------------------------------------
# Terminal v pycharm

"""
1. python manage.py startapp task - syzdava papka za app task
2. sled tova papkata q premesti v papkata na proekta kydeto e manage.py
3. registrirame task v settings.INSTALLED_APPS
"""

# Setting up a database

"""
v settings.DATABASES
trqbva ni 'adapter' za postgres - Psycopg2
pip install psycopg2

use database tab in pycharm
izbiram postgres i pisha samo user: postgres-user i pass: password, test connection, OK
click '1 of 4', click 'task_db', click 'default schema'
"""

# Models

"""
otivame v papka task i otvarqme models.py
modelite predstavlqvat standartni klasove
pravim gi

python manage.py makemigrations - proverqva django appovete i razliki sprqmo tekushtite migracii
syzdade fajl 0001_initial.py v task/migrations

python manage.py migrate - izpylnqva migraciite
syzdadeni sa tablici
sega veche ne trqbva da promenqme syzdadenite tablici ot pgadmin, a samo ot django!
"""

# Django Admin Site
"""
slagame administraciq kym nashiq application
dobavqneto na pyrviq potrebitel stava s komanda
python manage.py createsuperuser
daniel, daniel_zorov@abv.bg, Maimun06
http://127.0.0.1:8000/admin/
mogat da se dobavqt novi potrebiteli

registrirame v modula admin.py na task
"""

# Django View
"""
Cqlata biznes logika
Shte govorim za function based views
task.views.py
define function
create djangoProject101/task/urls.py
inside create variable urlpatterns

inside djangoProject101/urls.py (glavniq urls) syshto pishem

http://127.0.0.1:8000/task/

"""

# Templates
"""
imame django templates koito generirat dinamichno html

syzdavame index.html v papka templates
pravim funkciq vyv views.py
dobavqme v urls.py

put link in index.html:
<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
then right button on link and download locally


"""







