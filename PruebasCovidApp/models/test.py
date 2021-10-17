from django.db                  import models
from PruebasCovidApp.models.country import Country
from PruebasCovidApp.models.user import User

class Test(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    date = models.DateTimeField()
    result = models.CharField(max_length = 8)
    type = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)

