# Generated by Django 4.0 on 2023-02-19 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questoes', models.CharField(max_length=200, null=True)),
                ('opcao1', models.CharField(max_length=200, null=True)),
                ('opcao2', models.CharField(max_length=200, null=True)),
                ('opcao3', models.CharField(max_length=200, null=True)),
                ('opcao4', models.CharField(max_length=200, null=True)),
                ('respostaCorreta', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
