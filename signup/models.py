from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, db_index=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'Users'
        verbose_name_plural = "Users"
