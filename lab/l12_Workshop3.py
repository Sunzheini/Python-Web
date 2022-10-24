# Workshop: Part 3


"""
1. Create forms.py in pets/

2. Add:

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


sled tova nasledqvat:

class PetCreateForm(PetBaseForm):
    pass


3. Change 'add_pet' in pets/views.py to:

def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:       # POST
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)
    context = {
        'form': PetCreateForm(),
    }
    return render(request, 'pets/pet-add-page.html', context)


4. Change the template 'pet-add-page.html'

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


5. pravim edit:

def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug) \
        .get()
    if request.method == 'GET':
        form = PetEditForm(instance=pet)     # razlika s prednoto
    else:       # POST
        form = PetEditForm(request.POST, instance=pet)  # razlika s prednoto
        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)
    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-edit-page.html', context)


6. pet-edit-page.html:

        <!-- Start Edit Pet From -->
        <form action="{% url 'edit pet' username=username pet_slug=pet_slug %}" method="post">
            {{ form.as_p }}
            <button class="edit-btn" type="submit">Edit</button>
            {% csrf_token %}
        </form>
        <!-- End Edit Pet Form -->


7. delete formata

def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug) \
        .get()
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:       # POST
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details user ', pk=1)
    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-delete-page.html', context)


8. v html

        <!-- Starts Delete Pet Form -->
        <form method="post" action="{% url 'delete pet' username=username pet_slug=pet_slug %}">
            {{ form.as_p }}
            <button class="delete-btn" type="submit">Delete</button>
            <a class="btn btn-primary" href="javascript:history.back()">
                <button class="edit-btn" type="button">Go back</button>
            </a>
            {% csrf_token %}
        </form>
        <!-- End Delete Pet Form -->


8. configurirame dopylnitelno delete-a v forms:

class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance


9. Prodyljavame edit:

class PetEditForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


10. Create form_mixins.py in core/

class DisabledFormMixin:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'


11. Media files:

v settings.py:

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'mediafiles'


v urls.py:

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('petstagram.accounts.urls')),
    path('', include('petstagram.common.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('photos/', include('petstagram.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    )


12. photos / models.py:

upload_to='pet_photos/',

migrations and migrate


13. photo-item.html:

        </div>
    </div>

    <div class="imgBx" id="photo-{{ photo.pk }}">
        <img src="media/{{ photo.photo }}" alt="post" class="cover">
    </div>

    <div class="bottom">
        <div class="actionBtns">


14. in photos.photo database edit the file paths to begin with `pet_photos/`

15. create photos/forms.py ...
















"""
