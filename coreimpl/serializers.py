from rest_framework import serializers
from coreimpl.models import Accessories_sub_category ,Electronics,Fridge_ac_washingmachine,Furniture,Games_sub_category,Kitchen_other,Mobiles,Mobiles_sub_category,Motorcycles_sub_category,Other_vehicles_sub_category,Spare_parts_bikes_sub_category,Spare_parts_bikes_sub_category,Spare_parts_cars_sub_category,Tablets_sub_category,Bicycles_sub_category,Electronics,Fridge_ac_washingmachine,Bikes,Camera_sub_category,Cars,Cars_sub_category,Cars_sub_category,Commercial_vehicle_sub_category,Computer_sub_category


class Mobile_sub_MobileForm(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    mobile_brand_name= serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('tablets','tablets'),('accessories','accessories')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Mobiles_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class Mobile_sub_tablets_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    tablet_brand_name= serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('tablets','tablets'),('accessories','accessories')))
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Tablets_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    
class Mobile_sub_accessories_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    mobile_accessory_choice = serializers.CharField(max_length=250)
    accessory_brand_name =serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('mobile','mobile'),('tablets','tablets'),('accessories','accessories')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Accessories_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    


class Computer_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    computer_item_sub_category= serializers.CharField(max_length=250)
    computer_brand_name = serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('computer','computer'),('tvvideo','tvvideo'),('camera','camera'),('games','games'),('fridge','fridge'),('kitchen','kitchen')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Computer_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class Tv_video_sub_category_form(serializers.Serializer):
   title = serializers.CharField(max_length=250)
   price = serializers.IntegerField()
   description=serializers.CharField(max_length=500)
   photo = serializers.ImageField()
   name = serializers.CharField(max_length=250)
   phone_number = serializers.IntegerField()
   city = serializers.CharField(max_length=250)
   tv_video_sub_category=serializers.CharField(max_length=250)
   categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
   subcategories=serializers.ChoiceField(choices=(('computer','computer'),('tvvideo','tvvideo'),('camera','camera'),('games','games'),('fridge','fridge'),('kitchen','kitchen')))
   def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Tv_video_sub_category.objects.create(**validated_data)
        
   def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class Camera_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    camera_item_sub_category=serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('computer','computer'),('tvvideo','tvvideo'),('camera','camera'),('games','games'),('fridge','fridge'),('kitchen','kitchen')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Camera_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class Games_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    Games_item_sub_category=serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('computer','computer'),('tvvideo','tvvideo'),('camera','camera'),('games','games'),('fridge','fridge'),('kitchen','kitchen')))


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Games_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class Fridge_ac_washingmachine_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    Fridge_ac_washingmachine_sub_category=serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('computer','computer'),('tvvideo','tvvideo'),('camera','camera'),('games','games'),('fridge','fridge'),('kitchen','kitchen')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Fridge_ac_washingmachine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class Kitchen_other_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    Kitchen_other_sub_category=serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('computer','computer'),('tvvideo','tvvideo'),('camera','camera'),('games','games'),('fridge','fridge'),('kitchen','kitchen')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Kitchen_other.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class Cars_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    cars_brand_name = serializers.CharField(max_length=250)
    cars_model =serializers.CharField(max_length=250)
    kilometers_driven = serializers.IntegerField()
    year_manufacture = serializers.IntegerField()
    fuel = serializers.ChoiceField(choices=(('petrol','petrol'),('diesel','diesel'),('gas','gas')))
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('car','car'),('commercial','commercial'),('other','other'),('spare_cars','spare_cars')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Cars_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class Commercial_vehicle_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    commercial_vehicle_brand_name = serializers.CharField(max_length=250)
    kilometers_driven = serializers.IntegerField()
    year_manufacture = serializers.IntegerField()
    fuel = serializers.ChoiceField(choices=(('petrol','petrol'),('diesel','diesel'),('gas','gas')))
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('car','car'),('commercial','commercial'),('other','other'),('spare_cars','spare_cars')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Commercial_vehicle_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class Other_vehicles_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    Other_vehicles_brand_name = serializers.CharField(max_length=250)
    kilometers_driven = serializers.IntegerField()
    year_manufacture = serializers.DateField()
    fuel = serializers.ChoiceField(choices=(('petrol','petrol'),('diesel','diesel'),('gas','gas')))
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('car','car'),('commercial','commercial'),('other','other'),('spare_cars','spare_cars')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Other_vehicles_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class Spare_parts_cars_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    fuel = serializers.ChoiceField(choices=(('petrol','petrol'),('diesel','diesel'),('gas','gas')))
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('car','car'),('commercial','commercial'),('other','other'),('spare_cars','spare_cars')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Spare_parts_cars_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class Motorcycles_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    motorcycle_brand_name = serializers.CharField(max_length=250)
    bikes_model = serializers.CharField(max_length=250)
    kilometers_driven = serializers.IntegerField()
    year_manufacture = serializers.IntegerField()
    fuel = serializers.ChoiceField(choices=(('petrol','petrol'),('diesel','diesel'),('gas','gas')))
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('motorcycle','motorcycle'),('bicycle','bicycle'),('spare_bikes','spare_bikes')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Motorcycles_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class Bicycles_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    bicycle_brand_name = serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('motorcycle','motorcycle'),('bicycle','bicycle'),('spare_bikes','spare_bikes')))
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Bicycles_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class Spare_parts_bikes_sub_category_form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    spare_bikes_name = serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('motorcycle','motorcycle'),('bicycle','bicycle'),('spare_bikes','spare_bikes')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Spare_parts_bikes_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class Furniture_Form(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=250)
    furniture_type = serializers.CharField(max_length=250)
    categories=serializers.ChoiceField(choices=(('mobiles','mobiles'),('electronics','electronics'),('cars','cars'),('bikes','bikes'),('furniture','furniture')))
    subcategories=serializers.ChoiceField(choices=(('furniture','furniture'),('dummyfurniture','dummyfurniture')))

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Furniture.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance