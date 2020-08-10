from django.urls import path
from .views import product_list_view, product_detail_view

app_name = 'product'

urlpatterns = (
    path('all/', product_list_view, name='all'),
    path('detail/<int:pk>', product_detail_view, name='detail')
)