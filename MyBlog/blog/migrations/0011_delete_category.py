# Generated by Django 4.1.4 on 2022-12-25 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
