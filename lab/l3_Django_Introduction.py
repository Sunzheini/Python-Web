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
ima go v tools / run manage.py
i pishesh samo startapp task


2. sled tova papkata q premesti v papkata na proekta kydeto e manage.py
drag and drop i ok na refaktor


3. registrirame task v settings.INSTALLED_APPS
dobavqme go nakraq kato 'djangoProject102.departments'
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


4. create djangoProject101/task/urls.py
t.e. syzdavame urls.py v papkata na app-a
inside add: urlpatterns = ()
t.e. syzdavame prazen tuple


5. inside djangoProject101/urls.py (glavniq urls)
v urlpatterns dobavqme: 
    path('departments/', include('djangoProject102.departments.urls'))


6. inside views.py

create a function (view)
more info @ l4

a. 
def show_departments(request, *args, **kwargs):
    body = f'path: {request.path}, args={args}, kwargs={kwargs}'
    return HttpResponse(body)

def show_department_details(request, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)

b. 
mojem da dobavqme i parametri, v takiva skobi: <>
v urlpatterns dobavqme:
    path('<department_id>/', show_departments),
    path('int/<int:department_id>/', show_department_details),
    
tipovete sa: str, int, slug (human readable string), path, uuid

c.
view s render i promenlivi
  
def index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': random.random(),                           # promenliva, koqto vizulizirame v template
        'order_by': request.GET.get('order_by', 'name'),    # name e default parameter
        'info': {'address': 'Sofia'},                       # nested dict
        'student': Student('Daniel', 40),                   # moje info ot klas
    }
    return render(request, 'index.html', context)
# 'index.html' e template-a, koito shte napravim po-nadolu

d. 
redirect
def redirect_to_home(request):
return redirect('index')                                    # izpolzvame name='index'


7. v url.py
v urlpatterns dobavqme: 
    path('', index, name='index'),
    
otgore nad vsqko moje da slojish i linka, za da go cykash
http://127.0.0.1:8000/


"""

# Templates
"""
imame django templates koito generirat dinamichno html


10. syzdavame .....html v papka templates
hubavo e da se kazva kakto view-to

v nego ima:
    <h1>{{ title }}: {{ value }}</h1>
    {{ info.address }}      # za nested dict


    

put link in index.html:
<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
then right button on link and download locally


"""







