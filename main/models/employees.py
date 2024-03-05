from django.db import models
from main.models.positions import Position


class Employee(models.Model):
    first_name = models.CharField('First Name', max_length=64)
    last_name = models.CharField('Last Name', max_length=64)
    image = models.ImageField('Image', upload_to='images')
    birth_date = models.DateField('Birth Day')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
