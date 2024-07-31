import os

from django.db import models as md

from crm.settings import MEDIA_ROOT


class Product(md.Model):

    name = md.CharField(max_length=255, unique=True, db_index=True)
    description = md.TextField(blank=True)
    cost = md.DecimalField(max_digits=8, decimal_places=2)
    objects = md.Manager()

    def __str__(self):
        return self.name


class Advertisement(md.Model):

    name = md.CharField(max_length=255, unique=True, db_index=True)
    leads_count = md.IntegerField(default=0)
    customers_count = md.IntegerField(default=0)
    budget = md.DecimalField(max_digits=8, decimal_places=2)
    objects = md.Manager()
    profit = md.DecimalField(max_digits=20, decimal_places=2, default=0)
    ads_product = md.ForeignKey("Product", on_delete=md.SET_NULL, related_name="products", null=True)

    def __str__(self):
        return self.name


class Lead(md.Model):

    last_name = md.CharField(max_length=255, db_index=True)
    first_name = md.CharField(max_length=255, db_index=True)
    email = md.EmailField()
    phone = md.CharField(max_length=255, unique=True)
    objects = md.Manager()
    ads = md.ForeignKey("Advertisement", on_delete=md.CASCADE, related_name="leads")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def delete(self, using=None, keep_parents=False):
        try:
            ads = Advertisement.objects.get(pk=self.ads_id)
            ads.leads_count -= 1
            if self.customer:
                ads.customers_count -= 1
        except Lead.customer.RelatedObjectDoesNotExist:
            pass
        finally:
            ads.save()
            super().delete(using, keep_parents)


class Customer(md.Model):
    lead = md.OneToOneField("Lead", on_delete=md.CASCADE, related_name="customer")
    objects = md.Manager()

    def __str__(self):
        return f"{self.lead.first_name} {self.lead.last_name}"

    def delete(self, using=None, keep_parents=False):
        ads = Advertisement.objects.get(pk=self.lead.ads_id)
        ads.customers_count -= 1
        ads.save()
        super().delete(using, keep_parents)


class Contract(md.Model):
    name = md.CharField(max_length=255, unique=True, db_index=True)
    start_date = md.DateField()
    end_date = md.DateField()
    cost = md.DecimalField(max_digits=8, decimal_places=2)
    objects = md.Manager()
    customer = md.ForeignKey("Customer", on_delete=md.SET_NULL, related_name="contract", null=True)
    product = md.ForeignKey("Product", on_delete=md.SET_NULL, related_name="contracts", null=True)
    contract = md.FileField(upload_to="contracts/")

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        file_path = MEDIA_ROOT / self.contract.name
        if os.path.isfile(file_path):
            os.remove(file_path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        try:
            this = Contract.objects.prefetch_related('customer').prefetch_related('product').get(pk=self.pk)
            clean_file = this.contract.name
            if self.cost != this.cost:
                ad = this.customer.lead.ads
                ad.profit -= this.cost
                ad.profit += self.cost
                ad.save()
            if clean_file != self.contract:
                this.contract.delete(save=False)
        except (Contract.DoesNotExist, FileNotFoundError):
            super(Contract, self).save()
            res = Contract.objects.prefetch_related('customer').prefetch_related('product').get(pk=self.pk)
            ad = res.customer.lead.ads
            prof = res.cost - ad.budget - res.product.cost
            ad.profit += prof
            ad.save()
        else:
            super(Contract, self).save()
