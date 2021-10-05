from django.db import models
import datetime

# Create your models here.

class Register(models.Model):
    e_id=models.IntegerField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    post=models.CharField(max_length=200)
    salary=models.IntegerField()
    date=models.DateField(default=datetime.date.today)

    def __str__(self):
        name=self.name
        return name


