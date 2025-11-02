from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    pages_read = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    pages_total = models.IntegerField(validators=[MinValueValidator(1)])
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

def clean(self):
    from django.core.exceptions import ValidationError
    if self.pages_read > self.pages_total:
        raise ValidationError("Las páginas leídas no pueden ser mayores que el total de páginas.")
