from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    goal = models.DateField(null=True, blank=True)
    pages_read = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    pages_total = models.IntegerField(validators=[MinValueValidator(1)])
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True, default=None)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def progress(self):
        if self.pages_total == 0:
            return 0
        return round((self.pages_read / self.pages_total) * 100)
    
    def pages_for_day(self):
        if self.pages_total == 0:
            return 0
        tabla = []
        for dias in range(1, 11):
            paginas_por_dia = round(self.pages_total / dias)
            tabla.append((dias, paginas_por_dia))

        return tabla

def clean(self):
    from django.core.exceptions import ValidationError
    if self.pages_read > self.pages_total:
        raise ValidationError("Las páginas leídas no pueden ser mayores que el total de páginas.")
