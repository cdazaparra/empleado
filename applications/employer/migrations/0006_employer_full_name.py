# Generated by Django 4.2.6 on 2023-10-09 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0005_employer_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullName'),
        ),
    ]
