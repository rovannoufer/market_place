from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/',views.check_out, name="check_out"),
    path('update_item/',views.updateItem, name="update_item"),
    path('process_order/',views.processOrder, name="process_order"),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout')
]
