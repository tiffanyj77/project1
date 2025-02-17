from django.db import models
from django.contrib.auth.models import User


class SecurityQuestion(models.Model):
    answer = models.CharField(max_length=50)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.answer)
