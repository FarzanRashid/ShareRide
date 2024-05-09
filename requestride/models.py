from django.db import models
from signup.models import Users


class Requests(models.Model):
    pickup = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('signup.Users', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Requests'
        verbose_name_plural = "Requests"
