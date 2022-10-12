# Workshop2


"""
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

29. python manage.py makemigrations

30. Duplicate 0001_initial.py and name the duplicate to 0002_create_pet.py

31. In 0001_initial.py make the operations list empty:

    operations = [
    ]

32. In 0002_create_pet.py

delete this line:

    initial = True

add the dependencies:

    dependencies = [
        ('pets', '0001_initial')
    ]

33. Database --> Refresh

34. Click on "1 of 3" next to petstagram_db and select default schema

35. python manage.py migrate

and refresh database
* go to previous migration with 'manage.py migrate pets 0001'

36. Add a 4th field to class Pet(models.Model):

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=False,
    )

37. python manage.py makemigrations

    Select an option: 1
    >>> 'none'

38. python manage.py migrate

39. In pets/admin.py add:

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

40. python manage.py createsuperuser --username=daniel --email=daniel_zorov@abv.bg

    Password: Maimun06

    http://127.0.0.1:8000/admin/

41. Create a dog in admin

42. In pets/models.py, Pet(models.Model) add (to create a custom slug auto-generator):

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)

43. Change to 'blank=True':

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

44. python manage.py makemigrations
    python manage.py migrate

45. Because of the image fields we need to install:
    pip install Pillow

46. Make the second

    23
    24
    * Image fields:

    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',         # path to upload
        null=False,
        blank=True,
    )

    * Include also the relations, i.e.:

        tagged_pets = models.ManyToManyField(
            Pet,
            null=True,
        )

    * and validators:

        description = models.CharField(
            max_length=MAX_DESCRIPTION_LENGTH,
            validators=(
                MinLengthValidator(MIN_DESCRIPTION_LENGTH),
            ),
            null=True,
            blank=True,
        )

    29
    30
    31
    * but second time we made this also empty and made the empty lists tuples:
    dependencies = ()

    32
    * for the second module we also have dependancies from the first we worked on:
        dependencies = [
        ('pets', '0004_alter_pet_slug'),
        ('photos', '0001_initial'),
    ]

    35

    39
    41
    * add photo in admin:

    44


47. In order to add file (incl. images) size validator in photos/models.py:

add above the class:

    def validate_file_less_than_5mb(fileobj):
        filesize = fileobj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError(f"Max file size is {megabyte_limit}MB")

and change to (add the validators line):

    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

in photos/ create file validators.py and move the function there

make migrations and migrate

49. Add above pets/models.py, class Pet:

    class StrFromFieldsMixin:
        str_fields = ()

        def __str__(self):
            return '; '.join(
                f'{str_field}={getattr(self, str_field, None)}' for str_field in self.str_fields
            )

and add to inherit:

    class Pet(StrFromFieldsMixin, models.Model):
        str_fields = ('id', 'name')

then move the mixin to core/model_mixins.py

inherit also the others, i.e. photos / models.py, class Photo:

    class Photo(StrFromFieldsMixin, models.Model):
        str_fields = ('photo', 'location')

50. Replace in photos / admin.py with:

    @admin.register(Photo)
    class PhotoAdmin(admin.ModelAdmin):
        list_display = ('pk', 'publication_date', 'pets')

        @staticmethod
        def pets(current_photo_obj):
            tagged_pets = current_photo_obj.tagged_pets.all()
            if tagged_pets:
                return ', '.join(p.name for p in tagged_pets)
            return 'No pets'

51. Make the third: common / models.py, class PhotoComment and PhotoLike:

class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


52. Repeat:

    29
    30
    31
    32

    35


53. Changes in view, urls, models and htmls













"""
