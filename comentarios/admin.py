from django.contrib import admin
from .models import Comentario


# Register your models here.
class ComentatarioAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'usuario_comentario', 'nome_comentario', 'usuario_comentario', 'data_comentario', 'publicado_comentario')
    list_editable = ('publicado_comentario',)
    list_display_links = ('id', 'nome_comentario')


admin.site.register(Comentario, ComentatarioAdmin)
