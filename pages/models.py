from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name
    
        
class Furniture(models.Model):
    name = models.CharField(max_length=255)
    display_image = models.ImageField(upload_to='uploads/pics/furnitures')
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Bathroom(models.Model):
    number_of_bathroom = models.IntegerField()
    
    def __str__(self):
        return '{}'.format(self.number_of_bathroom)
    
class Bedroom(models.Model):
    number_of_bedroom = models.IntegerField()
    
    def __str__(self):
        return '{}'.format(self.number_of_bedroom)
    
class Garage(models.Model):
    number_of_garage = models.IntegerField()
    
    def __str__(self):
        return '{}'.format(self.number_of_garage)
    
class Rent(models.Model):
    title = models.CharField(max_length=255)
    choices = (
        ('Flat', 'Flat'),
        ('Hostel', 'Hostel'),
    )
    type = models.CharField(max_length=20, choices=choices, default="Flat")
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    display_image = models.ImageField(upload_to='uploads/pics/rent')
    image_1 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    image_2 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    image_3 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    image_4 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    image_5 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    bedroom = models.ForeignKey(Bedroom, on_delete=models.CASCADE)
    toilet_and_bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
      

class Sale(models.Model):
    title = models.CharField(max_length=255)
    choices = (
        ('Flat', 'Flat'),
        ('Estate', 'Estate'),
        ('Duplex', 'Duplex'),
    )
    type = models.CharField(max_length=20, choices=choices, default="Flat")
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State, default='All', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    display_image = models.ImageField(upload_to='uploads/pics/sale')
    image_1 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    image_2 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    image_3 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    image_4 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    image_5 = models.ImageField(upload_to='uploads/pics/rent', null=True, blank=True)
    bedroom = models.ForeignKey(Bedroom, on_delete=models.CASCADE)
    toilet_and_bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Land(models.Model):
    title = models.CharField(max_length=255)
    choices = (
        ('Any Land', 'Any Land'),
        ('50 x 100', '50 x 100'),
        ('100 x 100', '100 x 100'),
        ('100 x 200', '100 x 200'),
        ('200 x 200', '200 x 200'),
        ('1 acre', '1 acre'),
    )
    type = models.CharField(max_length=20, choices=choices, default="Any Land")
    price = models.FloatField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    display_image = models.ImageField(upload_to='uploads/pics/land')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    client_name = models.CharField(max_length=255)
    client_review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.client_name
    
class Social(models.Model):
    whatsapp = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    
    # def __str__(self):
    #     return 
    
    
    
    