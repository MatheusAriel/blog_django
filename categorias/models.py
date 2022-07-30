from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model):
    nome_cat = models.CharField(max_length=50, verbose_name='Categoria')
    status_cat = models.BooleanField(default=True, verbose_name='Status')
    data_criacao = models.DateTimeField(default=timezone.now)
    autor_cat = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, verbose_name='Autor')

    def __str__(self):
        return f'{self.nome_cat}'
