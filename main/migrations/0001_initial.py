# Generated by Django 3.2.4 on 2021-06-17 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('slug', models.SlugField(max_length=150, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('slug', models.SlugField(max_length=150, verbose_name='URL')),
                ('icon', models.FileField(upload_to='sous_cat/icons')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='main.category', verbose_name='Catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('slug', models.SlugField(max_length=150, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Déscription')),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('available', models.BooleanField(default=True, verbose_name='Disponible')),
                ('new', models.BooleanField(default=True, verbose_name='Nouveau')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo6', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo7', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo8', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo9', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('photo10', models.ImageField(blank=True, null=True, upload_to='images/produits')),
                ('sous_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.subcategory', verbose_name='Sous Catégorie')),
            ],
        ),
    ]
