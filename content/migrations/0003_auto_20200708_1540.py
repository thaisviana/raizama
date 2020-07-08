# Generated by Django 2.2.4 on 2020-07-08 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_produtor_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=40, null=True)),
                ('razao_social', models.CharField(max_length=40)),
                ('cnpj', models.CharField(blank=True, max_length=40, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('tipo', models.ManyToManyField(blank=True, related_name='organizacao_tipo', to='content.Tipo')),
            ],
        ),
        migrations.DeleteModel(
            name='Produtor',
        ),
    ]