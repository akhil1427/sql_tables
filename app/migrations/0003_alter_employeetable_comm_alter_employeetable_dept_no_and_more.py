# Generated by Django 4.2.6 on 2023-12-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_dept_salgrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetable',
            name='Comm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeetable',
            name='Dept_No',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employeetable',
            name='Empno',
            field=models.IntegerField(),
        ),
    ]
