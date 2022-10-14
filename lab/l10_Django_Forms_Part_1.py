# Django Forms - Part 1


"""
Web forms:

    formite poddyrjat samo GET i POST


Forms in Django

    generirame gi izpolzvaiki python kod



vyv views:

def index(request):
    name = None
    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']

        Person.objects.create(
            name=name,
        )

    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'index.html', context)


vyv web / forms/py:

from django import forms
class NameForm(forms.Form):
    your_name = forms.CharField(
        max_length=30,
    )


rychno v html:

<h1>
    {% if name %}
        Hello, {{ name }}! nice to see you!
    {% else %}
        Please, enter your name!
    {% endif %}
</h1>

{{ csrf_token }}
<form method="post" action="{% url 'index' %}">
    {{ form }}
    {% csrf_token %}
    <button>Send form</button>
</form>


pravim i model:

class Person(models.Model):
    name = models.CharField(
        max_length=30,
    )


kato vyvedesh ime vyv formata i go dobavq v db
"""


# explanations: form.is_valid(), ...
"""
form.is_valid()             # dali formata e validna, returns 'True', fills cleaned_data

form.cleaned_data           # rechnik, pazi dannite ot formata

help_text='Enter your name',
"""


# built-in widgets
"""
kak izglejdat nashite neshta

    widget=forms.Textarea() / .NumberInput() / email / password / url


dropdown, etc.:

occupancy = forms.ChoiceField(
    choices=...,                    # ot koe izbirame - list / tuple
    widget=forms.RadioSelect(),     # radio butoni
    
    widget=forms.CheckboxInput(),   # check box
    
    widget=forms.SelectMultiple()   
)


mojem dopylnitelno da gi pipvame v html

widget=forms.textInput(
    attrs={
        'placeholder': 'Enter name',        # default text in the field
        'class': 'form control',            # 
    }
)

posle moje v html da dobavim '.form-control..' i da promenqme formata
"""


# Django ModelForms Class
"""
auto generated forms ot modelite, pravqt dopylnitelni neshta

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person              # s koi model raboti
        fields = '__all__'          # izbirame all ili podavame spisyk ot neshta     
        
        
v model formite mojemd a podavame i widget-i

        widgets = ...   
        
"""






