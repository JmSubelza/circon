from django.db import models
from django.contrib.auth.models import User
from circon.warehouse.products.models import Products
from django.db import connection


class Purchase(models.Model):
    date_create = models.DateField(auto_now_add=True)
    date_purchase = models.DateField()
    n_purchase = models.CharField(max_length=10, blank=True)
    provider = models.ForeignKey(User)
    applicant = models.CharField(max_length=100, blank=True)
    observation = models.TextField(max_length=250, blank=True)
    base = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                               blank=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                              blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)
    status = models.CharField(max_length=1, default='0', blank=True)

    def __unicode__(self):
        return self.date_purchase.strftime('%d-%m-%Y')


class PurchaseDetail(models.Model):
    relationship = models.ForeignKey(Purchase)
    products = models.ForeignKey('products.Products')
    quantity = models.DecimalField(max_digits=100, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)

    def save(self, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("SELECT quantity FROM products_products WHERE id= %s", [self.products_id])
        row = cursor.fetchone()
        total = row[0] + self.quantity
        p = Products.objects.values('quantity').filter(id=self.products_id).update(quantity=total)
        super(PurchaseDetail, self).save(*args, **kwargs)
