from django.urls import path
from . import views
from .views import index, submit_product_view
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("sign", views.sign_view, name="sign"),
    path('submit/', submit_product_view, name='submit_product'),
    path('profile/', views.profile_view, name='profile'),
    path('delete/<int:product_id>/', views.delete_product_view, name='delete_product'),
      path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
      path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]