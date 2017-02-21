from django.shortcuts import render
from rest_framework import generics
from coreimpl.models import Accessories_sub_category,Electronics,Fridge_ac_washingmachine,Furniture,Games_sub_category,Kitchen_other,Mobiles,Mobiles_sub_category,Motorcycles_sub_category,Other_vehicles_sub_category,Spare_parts_bikes_sub_category,Spare_parts_bikes_sub_category,Spare_parts_cars_sub_category,Tablets_sub_category,Bicycles_sub_category,Electronics,Fridge_ac_washingmachine,Bikes,Camera_sub_category,Cars,Cars_sub_category,Cars_sub_category,Commercial_vehicle_sub_category,Computer_sub_category,Tablets_sub_category,Accessories_sub_category,Tv_video_sub_category

from coreimpl.serializers import Mobile_sub_MobileForm,Mobile_sub_tablets_form,Mobile_sub_accessories_form,Computer_sub_category_form,Tv_video_sub_category_form,Camera_sub_category_form,Games_sub_category_form,Fridge_ac_washingmachine_form,Kitchen_other_form,Cars_sub_category_form,Commercial_vehicle_sub_category_form,Other_vehicles_sub_category_form,Spare_parts_cars_sub_category_form,Motorcycles_sub_category_form,Bicycles_sub_category_form,Spare_parts_bikes_sub_category_form,Furniture_Form
# Create your views here.



class Mobile_sub_MobileFormList(generics.ListCreateAPIView):
    queryset = Mobiles_sub_category.objects.all()
    serializer_class = Mobile_sub_MobileForm

class Mobile_sub_tablets_formList(generics.ListCreateAPIView):
    queryset = Tablets_sub_category.objects.all()
    serializer_class = Mobile_sub_tablets_form

class Mobile_sub_accessories_formList(generics.ListCreateAPIView):
    queryset = Accessories_sub_category.objects.all()
    serializer_class = Mobile_sub_accessories_form

class Computer_sub_category_formList(generics.ListCreateAPIView):
    queryset = Computer_sub_category.objects.all()
    serializer_class = Computer_sub_category_form


class Tv_video_sub_category_formList(generics.ListCreateAPIView):
    queryset = Tv_video_sub_category.objects.all()
    serializer_class = Tv_video_sub_category_form

class Camera_sub_category_formList(generics.ListCreateAPIView):
    queryset = Camera_sub_category.objects.all()
    serializer_class = Camera_sub_category_form

class Games_sub_category_formList(generics.ListCreateAPIView):
    queryset = Games_sub_category.objects.all()
    serializer_class = Games_sub_category_form

class Fridge_ac_washingmachine_formList(generics.ListCreateAPIView):
    queryset = Fridge_ac_washingmachine.objects.all()
    serializer_class = Fridge_ac_washingmachine_form

class Kitchen_other_formList(generics.ListCreateAPIView):
    queryset = Kitchen_other.objects.all()
    serializer_class = Kitchen_other_form

class Cars_sub_category_formList(generics.ListCreateAPIView):
    queryset = Cars_sub_category.objects.all()
    serializer_class = Cars_sub_category_form


class Commercial_vehicle_sub_category_formList(generics.ListCreateAPIView):
    queryset = Commercial_vehicle_sub_category.objects.all()
    serializer_class = Commercial_vehicle_sub_category_form

class Other_vehicles_sub_category_formList(generics.ListCreateAPIView):
    queryset = Other_vehicles_sub_category.objects.all()
    serializer_class = Other_vehicles_sub_category_form

class Spare_parts_cars_sub_category_formList(generics.ListCreateAPIView):
    queryset = Spare_parts_cars_sub_category.objects.all()
    serializer_class = Spare_parts_cars_sub_category_form

class Motorcycles_sub_category_formList(generics.ListCreateAPIView):
    queryset = Motorcycles_sub_category.objects.all()
    serializer_class = Motorcycles_sub_category_form

class Bicycles_sub_category_formList(generics.ListCreateAPIView):
    queryset = Bicycles_sub_category.objects.all()
    serializer_class = Bicycles_sub_category_form

class Spare_parts_bikes_sub_category_formList(generics.ListCreateAPIView):
    queryset = Spare_parts_bikes_sub_category.objects.all()
    serializer_class = Spare_parts_bikes_sub_category_form

class Furniture_FormList(generics.ListCreateAPIView):
    queryset = Furniture.objects.all()
    serializer_class = Furniture_Form

