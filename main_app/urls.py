from django.urls import path
from . import views

urlpatterns = [
    # Static
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Stores
    path('stores/', views.stores_index, name='stores_index'),
    path('userstores/', views.user_stores, name='user_stores'),
    path('userstores/new/', views.new_store, name='new_store'),
    path('stores/<int:store_id>/', views.store_detail, name='store_detail'),
    path('stores/<int:store_id>/edit/', views.edit_store, name='edit_store'),
    path('stores/<int:store_id>/delete/', views.delete_store, name='delete_store'),
    # Candy
    path('candy/', views.candy_index, name='candy_index'),
    path('candy/<int:candy_id>/', views.candy_detail, name='candy_detail'),
    path('stores/<int:store_id>/candy/new/', views.add_candy, name='add_candy'),
    # Seller(user)
    path('accounts/signup/', views.signup, name='signup'),
]