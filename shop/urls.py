from django.urls import path

from shop.views import *

urlpatterns = [
    path('', index, name='home'),
    #path('contact/', contact)
    #path('category/<int:category_id>/', get_category, name='category')
    #path('category/<str:slug>/', ProductByCategory.as_view(), name='category'),
    #path('about/', about, name='about'),
    #path('category/', get_category, name='category')
    #path('products/', your_handler),
    #path('contacts/',),
]