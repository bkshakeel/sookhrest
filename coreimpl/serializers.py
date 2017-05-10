from rest_framework import serializers
from coreimpl.models import Accessories_sub_category ,Electronics,Fridge_ac_washingmachine,Furniture,Games_sub_category,Kitchen_other,Mobiles,Mobiles_sub_category,Motorcycles_sub_category,Other_vehicles_sub_category,Spare_parts_bikes_sub_category,Spare_parts_bikes_sub_category,Spare_parts_cars_sub_category,Tablets_sub_category,Bicycles_sub_category,Electronics,Fridge_ac_washingmachine,Bikes,Camera_sub_category,Cars,Cars_sub_category,Cars_sub_category,Commercial_vehicle_sub_category,Computer_sub_category,Tv_video_sub_category
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    Mobiles_sub_category = serializers.PrimaryKeyRelatedField(many=True, queryset=Mobiles_sub_category.objects.all())
    Tablets_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Tablets_sub_category.objects.all())
    Accessories_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Accessories_sub_category.objects.all())
    Computer_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Computer_sub_category.objects.all())
    Tv_video_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Tv_video_sub_category.objects.all())
    Camera_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Camera_sub_category.objects.all())
    Games_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Games_sub_category.objects.all())
    Fridge_ac_washingmachine= serializers.PrimaryKeyRelatedField(many=True, queryset=Fridge_ac_washingmachine.objects.all())
    Kitchen_other= serializers.PrimaryKeyRelatedField(many=True, queryset=Kitchen_other.objects.all())
    Cars_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Cars_sub_category.objects.all())
    Commercial_vehicle_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Commercial_vehicle_sub_category.objects.all())
    Other_vehicles_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Other_vehicles_sub_category.objects.all())
    Spare_parts_cars_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Spare_parts_cars_sub_category.objects.all())
    Motorcycles_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Motorcycles_sub_category.objects.all())
    Bicycles_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Bicycles_sub_category.objects.all())
    Spare_parts_bikes_sub_category= serializers.PrimaryKeyRelatedField(many=True, queryset=Spare_parts_bikes_sub_category.objects.all())
    Furniture= serializers.PrimaryKeyRelatedField(many=True, queryset=Furniture.objects.all())
    username=serializers.CharField(max_length=250)
    password=serializers.CharField(max_length=250)
    email=serializers.EmailField(allow_blank=False)

"""   def create(self, validated_data):
        print("in create")
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        print("user saved")
        return user"""


class Mobile_sub_MobileForm(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField(required=False)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.mobile_brand_name = validated_data.get('mobile_brand_name', instance.mobile_brand_name)
        instance.city = validated_data.get('city', instance.city)

        instance.save()
        return instance

    class Meta:
        fields = ('owner',)

class Mobile_sub_tablets_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.tablet_brand_name = validated_data.get('tablet_brand_name', instance.tablet_brand_name)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)

class Mobile_sub_accessories_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.mobile_accessory_choice = validated_data.get('mobile_accessory_choice', instance.mobile_accessory_choice)
        instance.accessory_brand_name = validated_data.get('accessory_brand_name', instance.accessory_brand_name)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)



class Computer_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.computer_item_sub_category = validated_data.get('computer_item_sub_category', instance.computer_item_sub_category)
        instance.computer_brand_name = validated_data.get('computer_brand_name', instance.computer_brand_name)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)

class Tv_video_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        return Tv_video_sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.tv_video_sub_category = validated_data.get('tv_video_sub_category', instance.tv_video_sub_category)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)



class Camera_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.camera_item_sub_category = validated_data.get('camera_item_sub_category', instance.camera_item_sub_category)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)



class Games_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.Games_item_sub_category = validated_data.get('Games_item_sub_category', instance.Games_item_sub_category)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


    class Meta:
        fields = ('owner',)

class Fridge_ac_washingmachine_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.Fridge_ac_washingmachine_sub_category = validated_data.get('Fridge_ac_washingmachine_sub_category', instance.Fridge_ac_washingmachine_sub_category)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)

class Kitchen_other_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.Kitchen_other_sub_category = validated_data.get('Kitchen_other_sub_category', instance.Kitchen_other_sub_category)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)


class Cars_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.kilometers_driven = validated_data.get('kilometers_driven', instance.phonkilometers_drivene_number)
        instance.year_manufacture = validated_data.get('year_manufacture', instance.year_manufacture)
        instance.fuel = validated_data.get('fuel', instance.fuel)
        instance.cars_brand_name = validated_data.get('cars_brand_name', instance.cars_brand_name)
        instance.cars_model = validated_data.get('cars_model', instance.cars_model)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)


class Commercial_vehicle_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.kilometers_driven = validated_data.get('kilometers_driven', instance.phonkilometers_drivene_number)
        instance.year_manufacture = validated_data.get('year_manufacture', instance.year_manufacture)
        instance.fuel = validated_data.get('fuel', instance.fuel)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)

class Other_vehicles_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.kilometers_driven = validated_data.get('kilometers_driven', instance.phonkilometers_drivene_number)
        instance.year_manufacture = validated_data.get('year_manufacture', instance.year_manufacture)
        instance.fuel = validated_data.get('fuel', instance.fuel)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)


class Spare_parts_cars_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.fuel = validated_data.get('fuel', instance.fuel)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)

class Motorcycles_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.motorcycle_brand_name = validated_data.get('motorcycle_brand_name', instance.motorcycle_brand_name)
        instance.bikes_model = validated_data.get('phone_number', instance.phone_number)
        instance.kilometers_driven = validated_data.get('kilometers_driven', instance.phonkilometers_drivene_number)
        instance.year_manufacture = validated_data.get('year_manufacture', instance.year_manufacture)
        instance.fuel = validated_data.get('fuel', instance.fuel)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)


class Bicycles_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.bicycle_brand_name = validated_data.get('bicycle_brand_name', instance.bicycle_brand_name)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)

class Spare_parts_bikes_sub_category_form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.IntegerField(read_only=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.spare_bikes_name = validated_data.get('spare_bikes_name', instance.spare_bikes_name)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)


class Furniture_Form(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username',default=User.objects.get(id=1))
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    description=serializers.CharField(max_length=500)
    photo = serializers.ImageField(required=True)
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
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.name = validated_data.get('name', instance.name)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.subcategories = validated_data.get('subcategories', instance.subcategories)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.furniture_type = validated_data.get('furniture_type', instance.furniture_type)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    class Meta:
        fields = ('owner',)