from django.db import models
from django.utils import timezone
from posts.models import Post
from django.contrib.auth.models import User


# Create your models here.
class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name="Nome")
    email_comentario = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Usuario")
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name="Data")
    publicado_comentario = models.BooleanField(default=False, verbose_name="Status")

    def __str__(self):
        return f'{self.usuario_comentario} - {self.nome_comentario}'
