from django.shortcuts import render
from rest_framework import generics
from coreimpl.models import Accessories_sub_category,Electronics,Fridge_ac_washingmachine,Furniture,Games_sub_category,Kitchen_other,Mobiles,Mobiles_sub_category,Motorcycles_sub_category,Other_vehicles_sub_category,Spare_parts_bikes_sub_category,Spare_parts_bikes_sub_category,Spare_parts_cars_sub_category,Tablets_sub_category,Bicycles_sub_category,Electronics,Fridge_ac_washingmachine,Bikes,Camera_sub_category,Cars,Cars_sub_category,Cars_sub_category,Commercial_vehicle_sub_category,Computer_sub_category,Tablets_sub_category,Accessories_sub_category,Tv_video_sub_category

from coreimpl.serializers import Mobile_sub_MobileForm,Mobile_sub_tablets_form,Mobile_sub_accessories_form,Computer_sub_category_form,Tv_video_sub_category_form,Camera_sub_category_form,Games_sub_category_form,Fridge_ac_washingmachine_form,Kitchen_other_form,Cars_sub_category_form,Commercial_vehicle_sub_category_form,Other_vehicles_sub_category_form,Spare_parts_cars_sub_category_form,Motorcycles_sub_category_form,Bicycles_sub_category_form,Spare_parts_bikes_sub_category_form,Furniture_Form
# Create your views here.
from coreimpl.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from coreimpl.permissions import IsOwnerOrReadOnly
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.views import LoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

    
class TwitterLogin(LoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter



class Mobile_sub_MobileFormList(generics.ListCreateAPIView):
    queryset = Mobiles_sub_category.objects.all()
    serializer_class = Mobile_sub_MobileForm
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Mobile_sub_tablets_formList(generics.ListCreateAPIView):
    queryset = Tablets_sub_category.objects.all()
    serializer_class = Mobile_sub_tablets_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Mobile_sub_accessories_formList(generics.ListCreateAPIView):
    queryset = Accessories_sub_category.objects.all()
    serializer_class = Mobile_sub_accessories_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Computer_sub_category_formList(generics.ListCreateAPIView):
    queryset = Computer_sub_category.objects.all()
    serializer_class = Computer_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class Tv_video_sub_category_formList(generics.ListCreateAPIView):
    queryset = Tv_video_sub_category.objects.all()
    serializer_class = Tv_video_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Camera_sub_category_formList(generics.ListCreateAPIView):
    queryset = Camera_sub_category.objects.all()
    serializer_class = Camera_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Games_sub_category_formList(generics.ListCreateAPIView):
    queryset = Games_sub_category.objects.all()
    serializer_class = Games_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Fridge_ac_washingmachine_formList(generics.ListCreateAPIView):
    queryset = Fridge_ac_washingmachine.objects.all()
    serializer_class = Fridge_ac_washingmachine_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Kitchen_other_formList(generics.ListCreateAPIView):
    queryset = Kitchen_other.objects.all()
    serializer_class = Kitchen_other_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Cars_sub_category_formList(generics.ListCreateAPIView):
    queryset = Cars_sub_category.objects.all()
    serializer_class = Cars_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class Commercial_vehicle_sub_category_formList(generics.ListCreateAPIView):
    queryset = Commercial_vehicle_sub_category.objects.all()
    serializer_class = Commercial_vehicle_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Other_vehicles_sub_category_formList(generics.ListCreateAPIView):
    queryset = Other_vehicles_sub_category.objects.all()
    serializer_class = Other_vehicles_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Spare_parts_cars_sub_category_formList(generics.ListCreateAPIView):
    queryset = Spare_parts_cars_sub_category.objects.all()
    serializer_class = Spare_parts_cars_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Motorcycles_sub_category_formList(generics.ListCreateAPIView):
    queryset = Motorcycles_sub_category.objects.all()
    serializer_class = Motorcycles_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Bicycles_sub_category_formList(generics.ListCreateAPIView):
    queryset = Bicycles_sub_category.objects.all()
    serializer_class = Bicycles_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Spare_parts_bikes_sub_category_formList(generics.ListCreateAPIView):
    queryset = Spare_parts_bikes_sub_category.objects.all()
    serializer_class = Spare_parts_bikes_sub_category_form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Furniture_FormList(generics.ListCreateAPIView):
    queryset = Furniture.objects.all()
    serializer_class = Furniture_Form
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)








class Mobile_sub_MobileFormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobiles_sub_category.objects.all()
    serializer_class = Mobile_sub_MobileForm
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Mobile_sub_tablets_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tablets_sub_category.objects.all()
    serializer_class = Mobile_sub_tablets_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Mobile_sub_accessories_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessories_sub_category.objects.all()
    serializer_class = Mobile_sub_accessories_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Computer_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computer_sub_category.objects.all()
    serializer_class = Computer_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)


class Tv_video_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tv_video_sub_category.objects.all()
    serializer_class = Tv_video_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Camera_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Camera_sub_category.objects.all()
    serializer_class = Camera_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Games_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games_sub_category.objects.all()
    serializer_class = Games_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Fridge_ac_washingmachine_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fridge_ac_washingmachine.objects.all()
    serializer_class = Fridge_ac_washingmachine_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Kitchen_other_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitchen_other.objects.all()
    serializer_class = Kitchen_other_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Cars_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars_sub_category.objects.all()
    serializer_class = Cars_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)


class Commercial_vehicle_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commercial_vehicle_sub_category.objects.all()
    serializer_class = Commercial_vehicle_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Other_vehicles_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Other_vehicles_sub_category.objects.all()
    serializer_class = Other_vehicles_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Spare_parts_cars_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spare_parts_cars_sub_category.objects.all()
    serializer_class = Spare_parts_cars_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Motorcycles_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Motorcycles_sub_category.objects.all()
    serializer_class = Motorcycles_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Bicycles_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bicycles_sub_category.objects.all()
    serializer_class = Bicycles_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Spare_parts_bikes_sub_category_formDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spare_parts_bikes_sub_category.objects.all()
    serializer_class = Spare_parts_bikes_sub_category_form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class Furniture_FormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all()
    serializer_class = Furniture_Form
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

