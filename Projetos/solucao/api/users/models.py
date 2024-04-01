from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 64)
    email = models.EmailField(max_length = 254)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

def __str__(self):
    return self.name