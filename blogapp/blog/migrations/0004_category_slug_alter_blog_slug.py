# Generated by Django 4.1 on 2022-09-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
