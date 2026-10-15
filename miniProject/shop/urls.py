from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop_view , name="shop_all"),
    path('watch/',views.shop_view ,{'category':'watch'}, name="shop_watch"),
    path('phone/',views.shop_view ,  {'category':'phone'},  name="shop_phone")


]
