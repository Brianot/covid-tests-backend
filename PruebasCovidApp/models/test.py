from re import T
from django.db                  import models
from PruebasCovidApp.models.country import Country
from PruebasCovidApp.models.user import User

class Test(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    user = models.ForeignKey(User, related_name = 'usuario', on_delete = models.CASCADE)
    country = models.ForeignKey(Country, related_name = 'pais', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True, blank = True)
    result = models.CharField(max_length = 8)
    type = models.CharField(max_length = 20)
    

