from django.contrib import admin
from django.urls import path
from mainApp import views as mainApp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.home),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shop),
    path('single-product/<int:id>',mainApp.singleProduct),
    path('price-range/<str:mc>/<str:sc>/<str:br>/',mainApp.priceRangeFilter),
    path('price-sort/<str:mc>/<str:sc>/<str:br>/<str:filter>/',mainApp.priceSortFilter),
    path('search/',mainApp.search),
    path('login/',mainApp.login),
    path('signup/',mainApp.signUp),
    path('profile/',mainApp.profile),
    path('logout/',mainApp.logout),
    path('update/',mainApp.update),
    path('add-to-cart/<int:num>/',mainApp.add_to_cart),
    path('remove-cart-item/<str:num>/',mainApp.remove_cart_item),
    path('update-cart/<str:num>/<str:op>/',mainApp.update_cart_page),
    path('add-to-wishlist/<int:num>/',mainApp.add_to_wishlist),
    path('remove-from-wishlist/<int:num>/',mainApp.remove_from_wishlist),
    path('wishlist/',mainApp.wishlist),
    path('cart/',mainApp.cart),
    path('checkout/',mainApp.checkout),
    path('place-order/',mainApp.place_order),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',mainApp.paymentSuccessPage),
    path('confirmation/',mainApp.confirmation),
    path('contact/',mainApp.contact),
    path('forget-password-1/',mainApp.forget_password_1),
    path('forget-password-2/',mainApp.forget_password_2),
    path('forget-password-3/',mainApp.forget_password_3),
    path('add-address/',mainApp.add_address_page),
    path('update-address/',mainApp.update_address),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)