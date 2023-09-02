from django.urls import path
from .views import index, top_sellers, advertisement_post, advertisement_post, advertisments_datail
from . import views
urlpatterns = [
    path('', index),
    path('glav/', index, name='glav'),
    path('top-sellers/', top_sellers, name='top_sellers'),
    path('advertisement-post/', advertisement_post, name='advertisement_post'),
    path('advertisement/<int:pk>', advertisments_datail, name="adv-detail"),
]

