# Generated by Django 4.2.2 on 2023-08-09 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_category_alter_recipe_cover_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='description',
            new_name='description',
        ),
    ]
