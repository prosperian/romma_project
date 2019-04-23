from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User

User.USERNAME_FIELD = 'email'
User.REQUIRED_FIELDS = ['username']
User._meta.get_field('username')._unique = False
User._meta.get_field('email')._unique = True


class Buy(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    month_plan = models.BooleanField(default=False)
    year_plan = models.BooleanField(default=False)
    started_at = models.DateTimeField(default=datetime.now)
    end_at = models.DateTimeField(default=datetime.now() + timedelta(days=30))

    def __str__(self):
        return self.created_by.username

