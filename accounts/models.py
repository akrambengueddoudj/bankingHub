from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    FREE = 'f'
    PAYED = 'p'
    BANK = 'b'
    USER_TYPE_CHOICES = [
        (FREE, "Free"),
        (PAYED, "Payed"),
        (BANK, "Bank")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    type = models.CharField(
        max_length=1, choices=USER_TYPE_CHOICES, default=FREE)
    payement_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " Profile"


class PayementRecipe(models.Model):
    ACCEPTED = 'a'
    REJECTED = 'r'
    NEW = 'n'
    STATUS_CHOICES = [
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
        (NEW, "New")
    ]
    TYPE_CHOICES = [
        ('client', "Client"),
        ('bank', "Bank")
    ]
    user_profile = models.ForeignKey(UserProfile,
                                     related_name="payements",
                                     on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/recipes/')
    recipe_type = models.CharField(
        max_length=30, choices=TYPE_CHOICES, default='client')
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=NEW)

    def __str__(self):
        return f"{self.status} - {self.user_profile.user}"


class Message(models.Model):
    user = models.ForeignKey(
        User, related_name="messages", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    subject = models.CharField(max_length=256, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
