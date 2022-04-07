# Generated by Django 3.1.1 on 2022-04-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220407_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]