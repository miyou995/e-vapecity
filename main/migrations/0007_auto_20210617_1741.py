# Generated by Django 3.2.4 on 2021-06-17 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210617_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('id',), 'verbose_name': 'Sous Catégorie', 'verbose_name_plural': 'Sous Catégorie'},
        ),
        migrations.RemoveField(
            model_name='treecategory',
            name='icon',
        ),
    ]
