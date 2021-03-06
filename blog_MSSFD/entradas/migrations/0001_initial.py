# Generated by Django 3.2.9 on 2021-12-15 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=300)),
                ('contenido', models.TextField(default='Texto del post')),
                ('img_destacada', models.FileField(upload_to='')),
                ('slug', models.CharField(default='DEFAULT VALUE', max_length=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
