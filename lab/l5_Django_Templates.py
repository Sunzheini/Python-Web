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


# custom tags
"""
    - simple tag - processes data and returns a string

slagame gi v application-a v package "templatetags" 
vytre fail tags.py


register = Library()

@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f"Hello, i am {student.name}"


sega moje da se izpolzva v template-a
{% load tags %}                        # trqbva da se importira imeto na faila v template-a

{% student_info student=student %}             # odd is the name of the filter


    # another 1

@register.simple_tag(name='sample_tag')
def sample_tag(*args, **kwargs):
    return ', '.join(str(x) for x in (list(args) + list(kwargs.items())))


{% sample_tag %}
{% sample_tag 17, 'Daniel', True %}
{% sample_tag department='engineering' %}


    - inclusion tag - processes data and returns a rendered template (kato mini view)

v templates direktoriq tags i fail nav.html

v tags.py:
@register.inclusion_tag('tags/nav.html' name='app_nav')
def general_nav(*args):
    context = {
        'url_names': args,
    }
    return

v index.html:
{% app_nav 'index' 'redirect_to_home' %}


moje da polchavame i context s takes_context=True:
@register.inclusion_tag('tags/nav.html' name='app_nav', takes_context=True)

"""


# Template inheritance
"""
pravim bazov template kydeto slagame placeholders (blocks)
v papka templates pravim papka base i pravim base.html

placeholder: 
{% block page_content %}        # page_content e imeto na bloka
..
{% endblock %}

v index.html (koito nasledqva bazoviq)
{% extends 'base/base.html' %}

{% block page_content %}        
 pishem nashiq text, koito overwriteva base-a
{% endblock %}

"""

# include template snippets
"""
"""


# statis files in Django
"""
statis files sa vsichki neshta v edin sait razlichni ot html koito se vizualizirat
css, javascript, kartinki

django ne se griji za statichnite failove po vreme na production

pravim papka staticfiles
vytre pravim site.css
v settings.py:
    STATIC_URL = '/static'  - pytq na koito iskame da gi dostypvame
    STATICFILES_DIRS = (    - direktoriiv koito ima statichni failove
        BASE_DIR / 'staticfiles',
    )

posle vkarvame css-a v html-a s:
{% load static %}
<link rel="stylesheet" href="{% static 'site.css' %}">

"""

# Bootstrap - biliboteka, koqto dava gotovi neshta za vizualizaciq
"""
include-vame css-a ot saita na bootstrap kakto gornoto



"""















