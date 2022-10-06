# Models in Django - Part 1


"""
1. Read data from database

vyv vies.py:

    def index(request):
        Employees.objects.all()     # dostypvame vsichki zapisi


objects e 'manager' i pozvolqva da se dostypqt dannite

'Employees.objects.all()' e query-set
strukturira sql zaqvkata, ne se izpylnqva na momenta, a kogato nqkoi q izpolzva


2. Filter

employees2 = Employees.objects.filter(age=23)
employees2 = Employees.objects.filter(age_lte=35)   # <=
...


3. You can chain

employees2 = Employees.objects.filter(age=23).order_by('last_name', 'first_name')
taka se izpylnqva v edna zaqvka kym bazata danni

employees2 = Employees.objects. \
    filter(age=23). \
    order_by('last_name', 'first_name')


4. Other

employees = Employees.objects.exclude(...)
employees = Employees.objects.get(pk=1)     # returns a single object not queryset
                                            # throws when multiple returns
                                            # only get is not lazy (executes now)
5. Delete

# views
def delete_employee(request, pk):
    employees = get_object_or_404(Employee, pk=pk)
    employees.delete()
    return redirect('index')


6. Class Meta - doopredelqt nashiq klas, pazi se info koqto doopisva modelite

v models vytre v klasa Employees!

    class Meta:
        ordering = ('-age', 'years_of_experience')


7. Abstract models - malko po-razlichni ot Python OOP

    class AuditInfoMixin(models.Model):

        class Meta:                 # nqma ABC
            abstract = True         # no table will be created in the DB
                                    # can be inherited in other models

8. Model methods

Mojem da pravim vsqkakvi


    def get_absolute_url(self): # kazva mi kakyv e url za da vidq info za daden odekt
        pass


9. Adding slugs - pravi se zaradi SEO

dobavqme kato metodite v modelite

    slug = models.SlugField(
        unique=True,
    )


sintaksisa na slug-a trqbva da e url compatible


10. Validators

if valid does nothing and if invalid raises validation error

make a function:

    def validate_before_today(value):
        if date.today < value:
            raise ValidationError()












"""



