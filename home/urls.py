from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_user, name='login'),
    #path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('display/<int:product_id>/<int:category_id>/', views.display, name='display'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('newproduct/', views.newproduct, name='newproduct'),
    path('newcat/',views.newcategory,name='newcategory'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='cartadd'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('cart_detail/remove/<int:product_id>/', views.remove_item, name='remove_item'),
]
 

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

