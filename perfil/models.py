from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    ddd = models.CharField(max_length=2)
    telefone = models.CharField(max_length=11)
    ddd_whatsapp = models.CharField(max_length=2)
    whatsapp = models.CharField(max_length=11)
    email = models.EmailField(max_length=60)
    data_nascimento = models.DateField()
    newsletter = models.BooleanField(default=False)
    status = models.CharField(
        max_length=1,
        default='A',
        choices=(
            ('A', 'Ativo'),
            ('I', 'Inativo'),
            ('B', 'Bloqueado'),
        ),
    )
    motivo_bloqueio = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}'

    def clean(self):
        pass

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
