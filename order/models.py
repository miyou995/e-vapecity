from django.db import models

# Create your models here.

from main.models import Product
class Order(models.Model):
    
    first_name  = models.CharField(verbose_name="Nom" , max_length=50, null=True, blank=True)
    last_name   = models.CharField(verbose_name="Prenom" , max_length=50, null=True, blank=True)
    addresse    = models.CharField(verbose_name="Adresse" , max_length=250, null=True, blank=True)
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25)
    email       = models.EmailField(null=True, blank=True)
    wilaya      = models.CharField(  max_length=50, null=True, blank=True)
    commune     = models.CharField(  max_length=50, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    birth_date  = models.DateField(verbose_name="Date de naissance")
    note        = models.TextField(blank=True, null=True)
    paid        = models.BooleanField(default=False)
    confirmer   = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Commande"
        ordering = ('-created',)

    def __str__(self):
        return f'commande N°:  {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order    = models.ForeignKey(Order,related_name='items', verbose_name=("Commande"), on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, verbose_name=("Commande"), on_delete=models.CASCADE)
    price    = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default = 1 )

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
