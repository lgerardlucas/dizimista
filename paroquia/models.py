from django.db import models

class Paroquia(models.Model):
    name = models.CharField('Nome da Paróquia', max_length=200, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Paróquia'    
        verbose_name_plural = 'Paróquias'
        ordering = ['name']

    def __str__(self):
        return self.name    