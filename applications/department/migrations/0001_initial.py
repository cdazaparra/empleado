# Generated by Django 4.2.6 on 2023-10-10 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameDepartment', models.CharField(max_length=50, verbose_name='nameDepartment')),
                ('shortNameDepartment', models.CharField(max_length=2, unique=True, verbose_name='shortNameDepartment')),
                ('activeDepartment', models.BooleanField(default=False, verbose_name='active')),
            ],
            options={
                'verbose_name': 'nameDepartment',
                'verbose_name_plural': 'nameDepartments',
                'ordering': ['nameDepartment'],
                'unique_together': {('nameDepartment', 'shortNameDepartment')},
            },
        ),
    ]
