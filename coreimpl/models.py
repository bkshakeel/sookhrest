from django.db import models
from django.utils import timezone

# Create your models here.
#modile category section
class Mobiles(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)
    subcategories = models.CharField(max_length=250,default='mobiles')
    categories = models.CharField(max_length=250,default='mobiles')
    created_time=models.DateTimeField(default=timezone.now)   

    class  Meta:
        abstract = True

class Mobiles_sub_category(Mobiles):
    owner = models.ForeignKey('auth.User', related_name='Mobiles_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    mobile_brand_name= models.CharField(max_length=250)

class Tablets_sub_category(Mobiles):
    owner = models.ForeignKey('auth.User', related_name='Tablets_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    tablets_brand_name =models.CharField(max_length=250)

class Accessories_sub_category(Mobiles):
    owner = models.ForeignKey('auth.User', related_name='Accessories_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    mobile_accessory_choice = models.CharField(max_length=250,default='mobile')
    accessory_brand_name =models.CharField(max_length=250)

#electronics section
class Electronics(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)
    subcategories = models.CharField(max_length=250,default='computer')
    categories = models.CharField(max_length=250,default='electronics')
    created_time=models.DateTimeField(default=timezone.now) 

    class  Meta:
        abstract = True

class Computer_sub_category(Electronics):
    owner = models.ForeignKey('auth.User', related_name='Computer_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    computer_item_sub_category= models.CharField(max_length=250)
    computer_brand_name = models.CharField(max_length=250)

class Tv_video_sub_category(Electronics):
    owner = models.ForeignKey('auth.User', related_name='Tv_video_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    tv_video_sub_category=models.CharField(max_length=250)

class Camera_sub_category(Electronics):
    owner = models.ForeignKey('auth.User', related_name='Camera_sub_category', on_delete=models.CASCADE)
    camera_item_sub_category=models.CharField(max_length=250)

class Games_sub_category(Electronics):
    owner = models.ForeignKey('auth.User', related_name='Games_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    Games_item_sub_category=models.CharField(max_length=250)

class Fridge_ac_washingmachine(Electronics):
    owner = models.ForeignKey('auth.User', related_name='Fridge_ac_washingmachine', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    Fridge_ac_washingmachine_sub_category=models.CharField(max_length=250)

class Kitchen_other(Electronics):
    owner = models.ForeignKey('auth.User', related_name='Kitchen_other', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    Kitchen_other_sub_category=models.CharField(max_length=250)

# cars section

class Cars(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)
    subcategories = models.CharField(max_length=250,default='car')
    categories = models.CharField(max_length=250,default='cars')
    created_time=models.DateTimeField(default=timezone.now)

    class  Meta:
        abstract = True

class Cars_sub_category(Cars):
    owner = models.ForeignKey('auth.User', related_name='Cars_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    cars_brand_name = models.CharField(max_length=250)
    cars_model = models.CharField(max_length=250)
    kilometers_driven = models.IntegerField()
    year_manufacture = models.IntegerField()
    fuel = models.CharField(max_length=250)

class Commercial_vehicle_sub_category(Cars):
    owner = models.ForeignKey('auth.User', related_name='Commercial_vehicle_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    commercial_vehicle_brand_name = models.CharField(max_length=250)
    kilometers_driven = models.IntegerField()
    year_manufacture = models.IntegerField()
    fuel = models.CharField(max_length=250)

class Other_vehicles_sub_category(Cars):
    owner = models.ForeignKey('auth.User', related_name='Other_vehicles_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    Other_vehicles_brand_name = models.CharField(max_length=250)
    kilometers_driven = models.IntegerField()
    year_manufacture = models.IntegerField()
    fuel = models.CharField(max_length=250)    

class Spare_parts_cars_sub_category(Cars):
    owner = models.ForeignKey('auth.User', related_name='Spare_parts_cars_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    spare_parts_category = models.CharField(max_length=250)

class Bikes(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)
    subcategories = models.CharField(max_length=250,default='bikes')
    categories = models.CharField(max_length=250,default='motorcycle')
    created_time=models.DateTimeField(default=timezone.now) 

    class  Meta:
        abstract = True


class Motorcycles_sub_category(Bikes):
    owner = models.ForeignKey('auth.User', related_name='Motorcycles_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    motorcycle_brand_name = models.CharField(max_length=250)
    bikes_model = models.CharField(max_length=250)
    kilometers_driven = models.IntegerField()
    year_manufacture = models.IntegerField()
    fuel = models.CharField(max_length=250)
    

class Bicycles_sub_category(Bikes):
    owner = models.ForeignKey('auth.User', related_name='Bicycles_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    bicycle_brand_name = models.CharField(max_length=250)

class Spare_parts_bikes_sub_category(Bikes):
    owner = models.ForeignKey('auth.User', related_name='Spare_parts_bikes_sub_category', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    spare_bikes_name = models.CharField(max_length=250)

class Furniture(models.Model):
    owner = models.ForeignKey('auth.User', related_name='Furniture', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    furniture_type = models.CharField(max_length=250)
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)
    categories=models.CharField(max_length=250,default='furniture')
    subcategories=models.CharField(max_length=250,default='furniture')
    created_time=models.DateTimeField(default=timezone.now)

