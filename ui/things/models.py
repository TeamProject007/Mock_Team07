from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from location_field.models.plain import PlainLocationField
# Create your models here.
WORK_CHOICES=(
    ("1", "Individual"),
    ("2", "Organisation"),
)
EMP_CHOICES=(
    ("1", "Employed"),
    ("2", "Unemployed"),
)
AFF_CHOICES=(
    ("1", "Yes"),
    ("2", "No"),
)

class Donor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    age=models.PositiveIntegerField()
    phoneno=PhoneField(blank=True,help_text='Contact phone number')
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    image=models.CharField(max_length=500,default='')
    choice=models.CharField(
        max_length = 20,
        choices = WORK_CHOICES,
        default = '1'
    )
    description=models.TextField()

class Donee(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    doname=models.CharField(max_length=256)
    doemail=models.EmailField(max_length=256)
    age=models.PositiveIntegerField()
    dophoneno=PhoneField(blank=True,help_text='Contact phone number')
    income=models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    dchoice=models.CharField(
        max_length = 20,
        choices = WORK_CHOICES,
        default = '1'
    )
    employment_status=models.CharField(
        max_length = 20,
        choices = EMP_CHOICES,
        default = '1'
    )
    affilated_with_NGO=models.CharField(
        max_length = 20,
        choices = AFF_CHOICES,
        default = '1'
    )

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name=models.CharField(max_length=200)
    item_quantity=models.PositiveIntegerField()
    item_image=models.CharField(max_length=500,default='https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F3%2F34%2FNokia_3310_3G_%252820180116%2529.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFeature_phone&tbnid=FjmqN9PVVRY7zM&vet=12ahUKEwibhsOs95XrAhV6k0sFHWCbBBEQMygHegUIARDyAQ..i&docid=Jtq_cpENzKzFCM&w=2166&h=2327&q=phone&ved=2ahUKEwibhsOs95XrAhV6k0sFHWCbBBEQMygHegUIARDyAQ')
    item_desc=models.TextField()

class Requirement(models.Model):

    def __str__(self):
        return self.requirement_name

    requirement_name=models.CharField(max_length=200)
    requirement_quantity=models.PositiveIntegerField()
    requirement_desc=models.TextField()
