# Django Templates


# Django template language + html --> Server-side rendering (SSR)

# <!-- This is html comment -->
"""
alternativa na django template ezika e jinja, no nie shte uchim DTL:
ima i drugi


    - variables

{{ variable }}

cannot have spaces, punctuation characters, dots, begin with underscore or be a number

funkciite se izpolzvat bez skobi - {{ function }}
syshto metodite ot klas


    - filters - transformirat dannite

{{ title | upper }} - pravi teksta uppercase

imame mnogo filers
{{ value|add:"2" }}

moje chain
{{ title|lower|capfirst }} - lower then capfirst
{{ 2|add:"3"|add:"4" }}

foramirane na data
{{ now|date:"y/M/d" }}


    - tags - Django Template Tagove: funkciq koqto raboti s nanshite danni

{% if my_list %}
    Number: {{ my_list|length }}
{% elif %}
    ...
{% endif %}

{% for student in students %}
    <li>{{ student }}</li>
{% endfor %}

{% for student in students %}
    <li>{{ student }}</li>
{% empty %}                 # ako nqma nishto v students
    <li>No students</li>
{% endfor %}


# url tag

<nav>
    <a href="">Go to index</a>
</nav>

<nav>
    <a href="{% url 'index' %}">Go to index</a>     # izpolzva django url-a, koito se kazva index
</nav>


# csrf token


    - comments

{# comment #} - single line

{% comment %} - multi line
...
...
{% endcomment %}
"""


# custom filters
"""
slagame gi v application-a v package "templatetags" 
vytre fail filters.py


register = Library()

@register.filter('odd')
def get_odd(values):
    return [x for x in values if x % 2 == 1]


sega moje da se izpolzva v template-a
{% load filters %}          # trqbva da se importira imeto na faila v template-a

{{ value|odd }}             # odd is the name of the filter
"""


# custom tags - -1:22
"""

"""




















