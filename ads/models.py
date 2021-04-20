from django.db import models

# Create your models here.
from django.urls import reverse

from users.models import Client, Employee


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    begin_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.client.last_name} by {self.employee.last_name}'

    def get_absolute_url(self):
        return reverse('contract-detail', args=[str(self.id)])

    class Meta:
        db_table = 'contracts'
        ordering = ['client', '-begin_date']


class Bill(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    print_date = models.DateTimeField(auto_now_add=True)
    sum = models.IntegerField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        if self.is_paid:
            return 'Bill paid'
        else:
            return 'Not paid'

    def get_absolute_url(self):
        return reverse('bill-detail', args=[str(self.id)])

    class Meta:
        db_table = 'bills'
        ordering = ['contract', '-print_date']


class BaseAd(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    efficiency = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


# TODO: add relative name
class OutdoorAd(BaseAd):
    height = models.IntegerField(default=1)
    width = models.IntegerField(default=1)
    type = models.CharField(max_length=100)
    contract = models.ManyToManyField(Contract)

    class Meta:
        db_table = 'outdoor_ads'

    def get_absolute_url(self):
        return reverse('outdoor-detail', args=[str(self.id)])


# TODO: add relative name
class TVAd(BaseAd):
    audience_coeff = models.IntegerField(default=100)
    duration = models.IntegerField(default=30)
    contract = models.ManyToManyField(Contract)

    class Meta:
        db_table = 'tv_ads'

    def get_absolute_url(self):
        return reverse('tv-detail', args=[str(self.id)])


# TODO: add relative name
class InternetAd(BaseAd):
    type = models.CharField(max_length=100, default='context_ad')
    contract = models.ManyToManyField(Contract)
    audience_coeff = models.IntegerField(default=100)
    specs = models.CharField(max_length=100, default='no specs')

    class Meta:
        db_table = 'internet_ads'

    def get_absolute_url(self):
        return reverse('internet-detail', args=[str(self.id)])
