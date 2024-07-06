from django.db import models


class Requests(models.Model):
    pickup = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('signup.Users', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
    matched_user = models.ForeignKey('signup.Users', null=True, blank=True,
                                     on_delete=models.SET_NULL, related_name='matched_requests')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Requests'
        verbose_name_plural = "Requests"
