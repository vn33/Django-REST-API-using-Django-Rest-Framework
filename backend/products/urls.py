from django.urls import path
from . import views

# api/products/
urlpatterns = [
    ## using mixin
    # path('', views.product_mixin_view),
    # path('<int:pk>/', views.product_mixin_view),
    # path('update/<int:pk>/', views.product_mixin_view),
    # path('delete/<int:pk>/', views.product_mixin_view),
    
    ## using generic
    path('', views.product_list_create_view),
    path('update/<int:pk>/', views.product_update_view),
    path('delete/<int:pk>/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view),
    
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view)
]