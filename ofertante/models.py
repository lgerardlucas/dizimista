from django.db import models

class Ofertante(models.Model):
    name = models.CharField('Nome do Dizimista', max_length=200, null=True, blank=True, unique=True)
    comunidade = models.ForeignKey('comunidade.Comunidade', on_delete=models.CASCADE, null=True, blank=True, related_name='comunidade', verbose_name='Comunidade')

    class Meta:
        verbose_name = 'Dizimista'
        verbose_name_plural = 'Dizimistas'
        ordering = ['name']

    def __str__(self):
        return self.name
