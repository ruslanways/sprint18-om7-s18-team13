# Generated by Django 3.1.1 on 2022-04-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20220407_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='patronymic',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]