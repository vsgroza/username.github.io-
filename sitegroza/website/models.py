from django.db import models

# Create your models here.


class Feeback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Message: {self.message}"