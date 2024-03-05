from django.db import models


class Position(models.Model):
    name = models.CharField('Name', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.name

