# Generated by Django 3.2.4 on 2021-06-17 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210617_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name': 'Catégorie', 'verbose_name_plural': 'Categories'},
        ),
    ]
