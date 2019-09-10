from django.db import models

# Create your models here.
class Kijakum(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f'{self.title}'