from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    AboutView,
    ShopListView,
    Terms,
    Privacy,
    Refunds,
    SellWithUs,
    Gallery,
    sell_with_us_two_form,
    ThankYouView
)
from . import views
app_name = 'core'

urlpatterns = [
    path('sell-with-us/', views.sell_with_us_two_form, name='sell-with-us'),
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('about/', AboutView.as_view(), name='about'),
    path('about.html', views.contact, name='contact'),
    path('shop-list/', ShopListView.as_view(), name='shop-list'),

    # Extras
    path('terms/', Terms.as_view(), name='terms'),
    path('privacy/', Privacy.as_view(), name='privacy'),
    path('refunds/', Refunds.as_view(), name='refunds'),
    path('thankyou/', ThankYouView.as_view(), name='thankyou'),

    # path('sellwithus/', SellWithUs.as_view(), name='sellwithus'),
    path('gallery/', Gallery.as_view(), name='gallery' )

]
