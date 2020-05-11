from django.conf import settings
from django.contrib.admin import *
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from backend.views import *


urlpatterns = [

    path('admin/', site.urls),
    path('', Home, name='home'),
    path('', Base, name='base'),
    path('register/', Register, name="register"),
    path('login/', Login, name='login'),
    path('logout/', Logout, name="logout"),
    path('products/', ProductList, name="allproducts"),
    path('sortedproducts/<keyword>', SortedProductList, name="sortedproducts"),
    path('usersortedproducts/<keyword>/', UserSortedProductList, name="usersortedproducts"),
    path('products/', UserProductList, name = 'productlist'),
    path('products/insert/', InsertProduct, name='insertproduct'),
    path('products/<int:product_id>/', product_detail, name="product_detail"),
    path('added/<int:product_id>/', add_to_cart, name="addtocart"),
    path('removed/<int:product_id>', remove_from_cart, name="removefromcart"),  
    path('cart/', ProfileCart, name="cart"),
    path('contact/', ContactForm, name="contact"),
    path('billing/', Billing, name="billing"),

    path('admindashboard/', AdminDashboard, name='admindashboard'),
    path('deleted/<int:product_id>', object_delete, name = "deleteobject"),
    path('admin/products/insert/', Admin_product_create, name = "productcreate"),
    path('admin/users', userlist, name = 'userlist'),
    path('admin/orders', admin_orders, name = 'orders'),

    path('<int:user_id>',user_detail, name = "profile_detail"),
    path('profile_edit/', edit_profile, name = 'editprofile'),
    path('change_password', change_password, name = 'change_password'),

    path('product_update/<int:product_id>', edit_product, name = 'product_update'),

    # payments
    path('charge/', charge, name="charge"),
    path("success/<str:args>", successMsg, name="success"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
