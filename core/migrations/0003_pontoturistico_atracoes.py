# Generated by Django 2.2 on 2020-05-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0002_auto_20200526_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracoes'),
        ),
    ]
