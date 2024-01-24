from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main, name='main'),
    path('me/', views.about_me, name='about_me'),
    path('client/<int:client_id>/', views.basket, name='basket'),
    path('client_sorted/<int:client_id>/<int:days_ago>/', views.sorted_basket, name='sorted_basket'),
    path('product_update/<int:product_id>', views.product_update_form, name='product_update'),
    path('product_update_id/', views.product_update_id_form, name='product_update_id'),
]