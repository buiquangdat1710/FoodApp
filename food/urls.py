from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    # food/
    path('', views.IndexClassView.as_view(), name='index'),
    # food/item
    path('item/', views.item, name = 'item'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('add', views.CreateItem.as_view(), name = "create_item"),
    path('update/<int:id>/', views.update_item, name = 'update_item'),
    path('delete/<int:id>/', views.delete_item, name = "delete_item"),
]
