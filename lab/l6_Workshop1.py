# Workshop: Part 1


"""
1. Create Project
2. Create apps: python manage.py startapp APP_NAME
3. Move all APPs to project folder
4. Create APP_NAME/urls.py with empty 'urlpatterns'
urlpatterns = (

)

5. Include APP_NAME/urls.py into project's urls.py
urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('petstagram.accounts.urls')),
]

6. Add APP_NAME to 'INSTALLED_APPS' in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'petstagram.accounts',
]

7. Subdirectories in 'templates' for each APP with the name of the app
8. Move html files in the respective subdirectories of 'templates'
9. 404.html and similar go to the main directory 'templates'
10. Go to views.py of each APP and create view for each template
    * don't use names for views like 'login', 'register', etc.
    ** for home, the view name is 'index'

def login_user(request):
    return render(request, 'accounts/login-page.html')

11. Go to urls.py of each APP
    * common parts must be combined using variables

urlpatterns = (
    # http://127.0.0.1:8000/accounts/login/
    path('login/', login_user, name='login user'),
    # http://127.0.0.1:8000/accounts/register/
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([
        # http://127.0.0.1:8000/accounts/profile/1/
        path('', details_user, name='details user'),
        # http://127.0.0.1:8000/accounts/profile/1/edit/
        path('edit/', edit_user, name='edit user'),
        # http://127.0.0.1:8000/accounts/profile/1/delete/
        path('delete/', delete_user, name='deletes user'),
    ])),
)

another example:

urlpatterns = (
    # http://127.0.0.1:8000/pets/add/
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        # http://127.0.0.1:8000/pets/daniel/pet/maxi/delete/
        path('delete/', delete_pet, name='delete pet'),
        # http://127.0.0.1:8000/pets/daniel/pet/maxi/
        path('', details_pet, name='details pet'),
        # http://127.0.0.1:8000/pets/daniel/pet/maxi/edit/
        path('edit/', edit_pet, name='edit pet'),
    ])),
)

12. Add the variable 'pk' to the respective views' input parameters

def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')

another example:

def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')

13. -1:20




















"""

