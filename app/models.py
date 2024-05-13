from django.db import models

class product(models.Model):
    name=models.CharField(max_length=25)
    id=models.IntegerField(primary_key=True)
    price=models.CharField(max_length=50)

    def __str__(self):
      return self.name