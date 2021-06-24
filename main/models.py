from django.db import models
from django.urls import reverse
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=150, verbose_name='Nom')
    slug = models.SlugField( max_length=150, verbose_name='URL')
    # pixel = models.TextField(verbose_name='Facebook Pixel', blank=True, null=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:prod-by-cat", args=[self.slug])

class TreeCategory(models.Model):
    name = models.CharField( max_length=150, verbose_name='Nom')
    slug = models.SlugField( max_length=150, verbose_name='URL')
    category = models.ForeignKey(Category, verbose_name="Catégorie",related_name="trees" ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Branche de Catégorie'
        verbose_name_plural = 'Branches de Catégorie'


class SubCategory(models.Model):
    name = models.CharField( max_length=150, verbose_name='Nom')
    slug = models.SlugField( max_length=150, verbose_name='URL')
    icon = models.FileField(upload_to='sous_cat/icons', max_length=100, verbose_name="icon de la Catégorie")
    tree = models.ForeignKey(TreeCategory, verbose_name="Branche de Catégorie",related_name="sub_categories" ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Sous Catégorie'
        verbose_name_plural = 'Sous Catégorie'
    
    def get_absolute_url(self):
        return reverse("main:prod-by-sub-cat", args=[self.slug])


# class SubCategory(models.Model):
#     name = models.CharField( max_length=150, verbose_name='Nom')
#     slug = models.SlugField( max_length=150, verbose_name='URL')
#     icon = models.FileField(upload_to='sous_cat/icons', max_length=100, verbose_name="icon de la Catégorie")
#     category = models.ForeignKey(Category, verbose_name="Catégorie",related_name="sub_categories" ,on_delete=models.CASCADE)






class Product(models.Model):
    name = models.CharField( max_length=150, verbose_name='Nom')
    slug = models.SlugField( max_length=150, verbose_name='URL', unique=True)
    sous_category = models.ForeignKey(SubCategory, verbose_name="Sous Catégorie",related_name="products" ,on_delete=models.CASCADE)
    description = tinymce_models.HTMLField(verbose_name='Déscription', blank=True, null=True)
    price   = models.DecimalField(max_digits=10, decimal_places=2, default=1)
   
    available = models.BooleanField(verbose_name='Disponible', default=True)
    new = models.BooleanField(verbose_name='Nouveau', default=True)
    top = models.BooleanField(verbose_name='Meilleur vente', default=True)
    created = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    photo1  = models.ImageField(upload_to='images/produits', blank=True, null=True)
    photo2  = models.ImageField(upload_to='images/produits', blank=True, null=True)
    photo3  = models.ImageField(upload_to='images/produits', blank=True, null=True)
    photo4  = models.ImageField(upload_to='images/produits', blank=True, null=True)
    photo6  = models.ImageField(upload_to='images/produits', blank=True, null=True)
    photo7  = models.ImageField(upload_to='images/produits', blank=True, null=True)
    photo8  = models.ImageField(upload_to='images/produits', blank=True, null=True)
    photo9  = models.ImageField(upload_to='images/produits', blank=True, null=True)
    photo10 = models.ImageField(upload_to='images/produits', blank=True, null=True) 
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def get_absolute_url(self):
        return reverse("main:productDetail", args=[self.slug])