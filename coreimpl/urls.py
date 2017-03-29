from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from coreimpl import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^rest-auth/twitter/$', views.TwitterLogin.as_view(), name='twitter_login'),
    url(r'^rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^mobiles/$', views.Mobile_sub_MobileFormList.as_view()),
    url(r'^tablets/$', views.Mobile_sub_tablets_formList.as_view()),
    url(r'^accessories/$', views.Mobile_sub_accessories_formList.as_view()),
    url(r'^computer/$', views.Computer_sub_category_formList.as_view()),
    url(r'^tv_video/$', views.Tv_video_sub_category_formList.as_view()),
    url(r'^camera/$', views.Camera_sub_category_formList.as_view()),
    url(r'^games/$', views.Games_sub_category_formList.as_view()),
    url(r'^fridge_ac_washingmachine/$', views.Fridge_ac_washingmachine_formList.as_view()),
    url(r'^kitchen/$', views.Kitchen_other_formList.as_view()),
    url(r'^cars/$', views.Cars_sub_category_formList.as_view()),
    url(r'^commercial_vehicle/$', views.Commercial_vehicle_sub_category_formList.as_view()),
    url(r'^other_vehicles/$', views.Other_vehicles_sub_category_formList.as_view()),
    url(r'^spare_parts_cars/$', views.Spare_parts_cars_sub_category_formList.as_view()),
    url(r'^motorcycles/$', views.Motorcycles_sub_category_formList.as_view()),
    url(r'^bicycles/$', views.Bicycles_sub_category_formList.as_view()),
    url(r'^spare_parts_bikes/$', views.Spare_parts_bikes_sub_category_formList.as_view()),
    url(r'^furniture/$', views.Furniture_FormList.as_view()),
   
    url(r'^mobiles/(?P<pk>[0-9]+)/$', views.Mobile_sub_MobileFormDetail.as_view()),
    url(r'^tablets/(?P<pk>[0-9]+)/$', views.Mobile_sub_tablets_formDetail.as_view()),
    url(r'^accessories/(?P<pk>[0-9]+)/$', views.Mobile_sub_accessories_formDetail.as_view()),
    url(r'^computer/(?P<pk>[0-9]+)/$', views.Computer_sub_category_formDetail.as_view()),
    url(r'^tv_video/(?P<pk>[0-9]+)/$', views.Tv_video_sub_category_formDetail.as_view()),
    url(r'^camera/(?P<pk>[0-9]+)/$', views.Camera_sub_category_formDetail.as_view()),
    url(r'^games/(?P<pk>[0-9]+)/$', views.Games_sub_category_formDetail.as_view()),
    url(r'^fridge_ac_washingmachine/(?P<pk>[0-9]+)/$', views.Fridge_ac_washingmachine_formDetail.as_view()),
    url(r'^kitchen/(?P<pk>[0-9]+)/$', views.Kitchen_other_formDetail.as_view()),
    url(r'^cars/(?P<pk>[0-9]+)/$', views.Cars_sub_category_formDetail.as_view()),
    url(r'^commercial_vehicle/(?P<pk>[0-9]+)/$', views.Commercial_vehicle_sub_category_formDetail.as_view()),
    url(r'^other_vehicles/(?P<pk>[0-9]+)/$', views.Other_vehicles_sub_category_formDetail.as_view()),
    url(r'^spare_parts_cars/(?P<pk>[0-9]+)/$', views.Spare_parts_cars_sub_category_formDetail.as_view()),
    url(r'^motorcycles/(?P<pk>[0-9]+)/$', views.Motorcycles_sub_category_formDetail.as_view()),
    url(r'^bicycles/(?P<pk>[0-9]+)/$', views.Bicycles_sub_category_formDetail.as_view()),
    url(r'^spare_parts_bikes/(?P<pk>[0-9]+)/$', views.Spare_parts_bikes_sub_category_formDetail.as_view()),
    url(r'^furniture/(?P<pk>[0-9]+)/$', views.Furniture_FormDetail.as_view()),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)