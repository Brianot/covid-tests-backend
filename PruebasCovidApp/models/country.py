from django.db.models.fields import BigAutoField
from django.db                  import models

class Country (models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length = 25)