# Generated by Django 3.1 on 2022-12-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posr',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='posr',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='posr',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]