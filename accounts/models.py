from django.db import models
from django.contrib.auth.models import User

class SecurityQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255)
    user = models.OneToOneField(User,
        on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username