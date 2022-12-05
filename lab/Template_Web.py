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

-----------------------------------------------------------------------------------

2. Create apps: python manage.py startapp web

3. Move all APPs to project folder

4. Create APP_NAME/urls.py with empty 'urlpatterns'
urlpatterns = (

)

5. Include APP_NAME/urls.py into project's urls.py
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('exam_prep_web_basics.web.urls')),    # add this only
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

-----------------------------------------------------------------------------------

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


    put at the top:

{% extends 'base.html' %}
{% block page_content %}

    -- here keep the content of the page --

    put at the botton:

{% endblock %}

    do it for all htmls, except base.html



    in base.html change all links to static:
        href="/static/css/styles.css">

    to:
        href="{% static '/css/styles.css' %}"   # keep `/css/styles.css` from above

    and on top:
        {% load static %}

    the same with all html files, also press load static

-----------------------------------------------------------------------------------

10. Go to views.py of each APP and create view for each template
    * don't use names for views like 'login', 'register', etc.
    ** for home, the view name is 'index'

!!! made names according to the urls in p.3 Routes in the files

def index(request):
    return render(request, 'accounts/login-page.html')

!!! I made:
•	http://localhost:8000/ - home page
•	http://localhost:8000/album/add/ - add album page
•	http://localhost:8000/album/details/<id>/ - album details page
•	http://localhost:8000/album/edit/<id>/ - edit album page
•	http://localhost:8000/album/delete/<id>/ - delete album page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/delete/ - delete profile page


def index(request):
    return render(request, 'core/home-with-profile.html')


def details_album(request, pk):
    return render(request, 'albums/album-details.html')


def add_album(request):
    return render(request, 'albums/add-album.html')


def edit_album(request, pk):
    return render(request, 'albums/edit-album.html')


def delete_album(request, pk):
    return render(request, 'albums/delete-album.html')


def details_profile(request):
    return render(request, 'profiles/profile-details.html')


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')
!!!

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

!!! napravih:

# 	http://localhost:8000/ - home page
# •	http://localhost:8000/album/add/ - add album page
# •	http://localhost:8000/album/details/<id>/ - album details page
# •	http://localhost:8000/album/edit/<id>/ - edit album page
# •	http://localhost:8000/album/delete/<id>/ - delete album page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/delete/ - delete profile page


from django.urls import path, include

from exam_prep_web_basics.web.views import index, add_album, details_album, edit_album, delete_album, details_profile, \
    delete_profile

urlpatterns = (
    # http://localhost:8000/
    path('', index, name='index'),

    path('album/', include([
        # http://localhost:8000/album/add/
        path('add/', add_album, name='add album'),
        # http://localhost:8000/album/details/<id>/
        path('details/<int:pk>/', details_album, name='details album'),
        # http://localhost:8000/album/edit/<id>/
        path('edit/<int:pk>/', edit_album, name='edit album'),
        # http://localhost:8000/album/delete/<id>/
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),

    path('profile/', include([
        # http://localhost:8000/profile/details/
        path('details/', details_profile, name='details profile'),
        # http://localhost:8000/profile/delete/
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
!!!

12. Add the variable 'pk' to the respective views' input parameters

def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')

another example (slugs are also parameters):

def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')

!!! added it in 10.


23. Open pets/models.py

24. Create the needed class (table) and class attributes (fields)

class Pet(models.Model):
    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

if the field is required:
null=False,
blank=False,

if the field is optional:
null=True,
blank=True,

integer field >= 0:
age = models.PositiveIntegerField()

inache za float >= 0.0:
validators=(
            validators.MinValueValidator(0.0),
        ),

for min values:
        validators=(
            validators.MinLengthValidator
        )

unikalen:
unique=True,


kogato imame choice:
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other Music'

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    genre = models.CharField(
        max_length=MAX_GENRE_NAME_LENGTH,
        null=False,
        blank=False,
        choices=MUSICS,
    )


if 	The username can consist only of letters, numbers, and underscore ("_"):
def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")

class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_only_alphanumeric,
        ),
        null=False,
        blank=False,
    )


after each model: python manage.py makemigrations (bez migrate!)

-----------------------------------------------------------------------------------

25. Replace in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'petstagram_db',         # should be the same name as the DB created below
        'USER': 'postgres-user',
        'PASSWORD': 'password',
        'HOST': 'localhost',    # Not host.docker.internal - only for pgadmin
        'PORT': '5432',
    }
}

26. pip install psycopg2

27. Database Menu in PyCharm

    Database --> + --> Data Source --> PostresSql
    --> User: postgres-user, Pass: password --> Test Connection --> Ok

    Rightclick on postgres@localhost --> New --> Database --> Name it --> Ok

28. python manage.py migrate

33. Database --> Refresh

34. Click on "1 of 3" next to petstagram_db and select default schema


# From the file: 4. Pages:
# ------------------------------------------------------------------------------------#
# base.html:

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


!!! za d anapravim tova:

•	The "Home" button leads to the home page.
•	The "Create Album" button leads to create album page.
•	The "Profile" button leads to the profile page.

opravqme linkovete v base.html:

napr. tova:
<a href="#">Home</a>

na:
<a href="{% url 'index' %}">Home</a>    # `index` e naimenovanieto `name=` v urls.py
!!!

# Home Page

!!! korekcii:
dobavq,e v urls.py:

    path('profile/', include([
        path('add/', add_profile, name='add profile'),  # tova

dobavqme vyv views.py:

def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None

def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')
    return render(request, 'core/home-with-profile.html')

def add_profile(request):
    return render(request, 'core/home-no-profile.html')

-----------------------------------------------------------------------------------

39. In admin.py add:

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

!!! added:
from exam_prep_web_basics.web.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
!!!


40. python manage.py createsuperuser --username=daniel --email=daniel_zorov@abv.bg

    Password: Maimun06

    http://127.0.0.1:8000/admin/

41. Create a dog in admin

!!! syzdadohme  profil


54. Create forms.py in pets/

!!! t.k. atributite koito se iskat vyv formata sa
!!! syshtite kato na modela Profile, pravim model form

55. Add:

from django import forms # not forms.forms!!!

# obsht roditel:
class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # fields = '__all__'
        fields = (
            'name',
            'date_of_birth',
            'personal_photo',
        )
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {     # the placeholders
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }

!!! napravihme:
from django import forms
from exam_prep_web_basics.web.models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
!!!


# tova ne sme
# --------------------------------------
sled tova nasledqvat:

class PetCreateForm(PetBaseForm):
    pass
# --------------------------------------


56. Change 'add_pet' in pets/views.py to:

def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:       # POST
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context)

!!! we changed add_profile to:

def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)
!!!

# core/home-no-profile.html

57. Change the template 'pet-add-page.html'

change this:

       <!-- Start Add Pet Form -->
        <form action="#">
            <p>
                <label for="pet-name">Pet name: </label>
                <input type="text" placeholder="Pet name">
            </p>
            <p>
                <label for="pet-date">Date of birth: </label>
                <input type="date">
            </p>
            <p>
                <label for="pet-image">Link to image: </label>
                <input type="text" placeholder="Link to image">
            </p>
            <!-- Add Pet Button -->
            <button class="add-btn" type="submit">Add Pet</button>
        </form>
        <!-- End Add Pet Form -->

to this:

        <!-- Start Add Pet Form -->
        <form action="{% url 'add pet' %}" method="post">
            {{ form.as_p }}
            <button class="add-btn" type="submit">Add Pet</button>
            {% csrf_token %}
        </form>
        <!-- End Add Pet Form -->

!!! changed this:

    <section id="registerPage">
        <form>
            <fieldset>
                <legend>Profile</legend>
                <!-- Form for Registration -->
                <label for="username">Username:</label>
                <input id="username" name="username" type="text" placeholder="Username">

                <label for="email">Email:</label>
                <input id="email" name="email" type="email" placeholder="Email">

                <label for="age">Age:</label>
                <input id="age" name="age" type="number" min="0" placeholder="Age">
                <!-- Button to Create Profile -->
                <button type="submit" class="register">Enter</button>
            </fieldset>
        </form>
    </section>

to:

    <section id="registerPage">
        <form>
            <fieldset>
                <legend>Profile</legend>
                {{ form }}                          # this
                <button type="submit" class="register">Enter</button>
                {% csrf_token %}                    # this
            </fieldset>
        </form>
    </section>





"""