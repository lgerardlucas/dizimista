from django.db import models

class Comunidade(models.Model):
    name = models.CharField('Nome da Comunidade', max_length=200, null=True, blank=True, unique=True)
    paroquia = models.ForeignKey('paroquia.Paroquia', on_delete=models.CASCADE, null=True, blank=True, related_name='paroquia', verbose_name='Paróquia')

    class Meta:
        verbose_name = 'Comunidade'
        verbose_name_plural = 'Comunidades'
        ordering = ['name']

    def __str__(self):
        return self.name
