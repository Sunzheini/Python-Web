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
"""







# 1:45:00h (zapochnahme v 6:40 i mina edna pochivka 15min)








