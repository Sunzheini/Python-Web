# Django Forms - Part 2


# Django Validators
"""
pravim funkciq za proverka na nevalidnite scenarii

def validate_text(value):
    if '_' in value:
        raise ValidationException('`_` is invalid char')


class ToDoForm(forms.Form):
text = forms.CharField(
        validators=(
            validate_text,
        ),
    )
"""

# built-in validatori

"""
class ToDoForm(forms.Form):
text = forms.CharField(
        validators=(
            MinValueValidator(),
        ),
    )
"""

# validatori s klasove
"""
@deconstructible
class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.max_value = max_value
        self.min_value = min_value
        
    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(f"Message")
        
    def __eq__(self, other):
        return(
                isinstance(other, self.__class__)
                and self.min_value == other.min_value            
        )
"""

# modelform validators
"""
clean() metodi - transform data into desired format (lower / upper)
               - validation
"""

# error messages
"""
"""


# ---------------------------------------------------------------------------
# Media Files - 58:28

"""
media files - stitichni failove kacheni ot potrebitelite (te mogat da gi kachvat)

failovete gi pravi na string i gi prashta na syrvyra


uninstall PIL then install Pillow
Pillow - poddyrja uploadvane na takiva failove


profile_image = models.ImageField(null=True, blank=False, upload_to'')
profile_image = models.FileField(null=True, blank=False, upload_to'')    # za vsqkakvi failove

upload_to - v koq direktoriq
"""





