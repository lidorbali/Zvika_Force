from django.urls import path
from . import views
from .views import MyTokenObtainPairView, addCats

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
  
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register),
    path('logout/',views.myLogout),

    path('add_product/', views.addProduct),
    path('add_cats/', views.addCats),
    path('addOrder/', views.addOrder),
    path('categories/', views.getCats),
    path('products/<id>', views.getProduct),
    path('products/', views.getProduct),
    

]
