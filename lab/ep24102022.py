"""
0. place files: static on the same level as 'exam_prep_web_basics'
   and htmls from 'templates' in templates/


13. Next to 'templates' create a folder 'staticfiles'
!!! we renamed static to staticfiles

14. Go to settings.py and add:

STATIC_URL = 'static/'              # files are accesses @ static

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',       # files are located @ staticfiles
)


2. Create apps: python manage.py startapp web

3. Move all APPs to project folder

4. Create APP_NAME/urls.py with empty 'urlpatterns'
urlpatterns = (

)

5. Include APP_NAME/urls.py into project's urls.py
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('exam_prep_web_basics.urls')),    # add this only
]

6. Add APP_NAME to 'INSTALLED_APPS' in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'exam_prep_web_basics.web',      # add this only: project_name / app_name
]

7. Subdirectories in 'templates' for each APP with the name of the app
!!! tuk t.k. imame 1 app razdelihme html v podpapki albums, profiles i core

8. Move html files in the respective subdirectories of 'templates'

9. 404.html and similar go to the main directory 'templates'
!!! n/a

15. In each html the path must point to static/ not staticfiles/ !
i.e. href="/static/css/styles.css">

16. Combine the common parts: using Template Inheritance:
    make directory 'base' in 'templates'
    !!! n/a

    make base.html
    !! provided with exam prep

    put inside base.html the common things, without main, where we replace the contents of main with a block:
<main>
    {% block page_content %}
    {% endblock %}
</main>
    !!! we did this instead:

replace in base.html this:
    </header>
    <!-- End Navigation Bar -->

    <!-- Main Content -->

    <!-- Footer -->
    <footer>

to this:
    </header>
    <!-- End Navigation Bar -->

    <!-- Main Content -->
    {% block content %}         # add this
    {% endblock %}              # add this
    <!-- Footer -->
    <footer>


didnt do it yet
# -------------------------------------
    put at the top:

{% extends 'base/base.html' %}
{% block page_content %}

    put at the botton:

{% endblock %}

    do it for all htmls, except base.html
# -------------------------------------


    in base.html change all links to static:
        href="/static/css/styles.css">

    to:
        href="{% static '/css/styles.css' %}"   # keep `/css/styles.css` from above

    and on top:
        {% load static %}

    the same with all html files, also press load static


10. Go to views.py of each APP and create view for each template
    * don't use names for views like 'login', 'register', etc.
    ** for home, the view name is 'index'

def login_user(request):
    return render(request, 'accounts/login-page.html')


# 3:01:47















"""