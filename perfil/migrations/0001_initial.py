# Generated by Django 3.0.8 on 2020-08-03 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('ddd', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=9)),
                ('ddd_whatsapp', models.CharField(max_length=2)),
                ('whatsapp', models.CharField(max_length=9)),
                ('data_nascimento', models.DateField(null=True)),
                ('status', models.CharField(default='A', max_length=1)),
                ('novidades', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
            },
        ),
    ]
