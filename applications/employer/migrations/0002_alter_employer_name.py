# Generated by Django 4.2.6 on 2023-10-07 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]
