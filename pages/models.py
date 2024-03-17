from django.db import models
from django.contrib.auth.models import User


class FinancialConsulting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    is_responded = models.BooleanField(default=False)
    response = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username + " - Consulting"


class Banks(models.Model):
    bank_name = models.CharField(max_length=256, null=False, unique=True)

    def __str__(self):
        return self.bank_name


class BankBranch(models.Model):
    name = models.CharField(max_length=256)
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)


class BankCity(models.Model):
    name = models.CharField(max_length=256)
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)
    branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    city = models.ForeignKey(BankCity, on_delete=models.CASCADE)
    barcode_image = models.ImageField(
        upload_to='barcodes/', null=True, blank=True)
    date_time = models.DateTimeField()


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)


class ServicePictures(models.Model):
    service = models.ForeignKey(
        Service, related_name='pictures', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="images/service/")
