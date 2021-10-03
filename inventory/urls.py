from django.urls import path
from inventory import views

urlpatterns = [
    path('items/', views.ItemList.as_view(), name="item-list"),
    path('items/<int:pk>', views.ItemDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>', views.CategoryDetail.as_view()),
]
