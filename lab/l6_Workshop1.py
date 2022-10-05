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

another example (slugs are also parameters):

def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')

13. Next to 'templates' create a folder 'staticfiles'
14. Go to settings.py and add:

STATIC_URL = 'static/'              # files are accesses @ static

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',       # files are located @ staticfiles
)

15. In each html the path must point to statis/ not staticfiles/ !
i.e. href="/static/css/styles.css">

16. Combine the common parts: using Template Inheritance:
    make directory 'base' in 'templates'
    make base.html
    put inside the common things, without main, where we replace the contents of main with a block:

<main>
    {% block page_content %}
    {% endblock %}
</main>

    put at the top:

{% extends 'base/base.html' %}
{% block page_content %}

    put at the botton:

{% endblock %}

    do it for all htmls, except base.html
    in base.html change:

        href="/static/css/styles.css">

    to:

        href="{% static 'css/styles.css' %}"

    and on top:

        {% load static %}

    the the same with:

        href="/static/images/free-30-instagram-stories-icons23_122570.png"
        href="{% static 'images/free-30-instagram-stories-icons23_122570.png' %}"

        src="/static/images/free-30-instagram-stories-icons23_122570.png" alt="img1"
        src="{% static 'images/free-30-instagram-stories-icons23_122570.png'%}"
                     alt="img1">

    the same with all html files, also press load static

17. In 'base' make folder 'partials' and inside - nav.html

18. Put inside from base.html:

<nav class="navbar">
    ...
    </nav>

19. Replace in base.html with following:

{% include 'base/partials/nav.html' %}

20. Where we have:

        <!-- Link to Home Page -->
        <a href="#">
            <img width="50px"
                    src="{% static 'images/free-30-instagram-stories-icons23_122570.png'%}"
                    alt="img1">
        </a>

    change:

        <a href="#">

    to:

        <a href="{% url 'index' %}">  # using the names of the urls that we made previously

    if we have parameters, to:

        <a href="{% url 'details user' pk=1 %}">    # currently hardcoding pk

21. Fix all other urls:

    change:

        <a href="#">

    to (for example):

        <a href="{% url 'details user' pk=1 %}">

    on this stage we cannot fix all of them (at a later stage of the workshop)

22. Editing 404.html

in settings.py:

    DEBUG = False

    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
    ]

but styles are not loaded now, so we type in terminal:

    python manage.py runserver --insecure

then in 404.html:

    {% extends 'base/base.html' %}
    {%  block page_content %}

    contents of main

    {% endblock %}

    fix the static link and the url link

change back to: DEBUG = True

23.
























"""

