from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('fruits/', views.fruits, name="fruits"),
	path('vegetables/', views.vegetables, name="vegetables"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('search_result/', views.searchResult, name="search_result"),
	path('seller_register/', views.SellerRegister, name="seller_register"),
	path('buyer_register/', views.BuyerRegister, name="buyer_register"),
	path('seller_login/', views.SellerLogin, name="seller_login"),
	path('buyer_login/', views.BuyerLogin, name="buyer_login"),
	path('profile/', views.Profile, name="profile"),
	path('order_status/', views.OrderStatus, name="order_status"),
	path('logout/', views.logoutUser, name="logout"),
	path('seller_home/', views.SellerHome, name='seller_home'),
	path('home/',views.Home, name="home"),
]