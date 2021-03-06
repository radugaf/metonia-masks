from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField

CATEGORY_CHOICES = (
    ('S', 'Luxury'),
    ('SW', 'Casual'),
    ('OW', 'Dinner Party')
)

LABEL_CHOICES = (
    ('P', 'Special Offer'),
    ('S', 'Limited Edition'),
    ('D', 'New Collection'),
    ('N', 'Sold Out')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

STARE_CHOICES = (
    ('NE', 'Noua cu Etichete'),
    ('Noua Fara Etichete', 'Noua Fara Etichete'),
    ('Foarte Buna', 'Foarte Buna'),
    ('Buna', 'Buna'),
    ('Purtata', 'Purtata'),
    ('Prezinta Mici Defecte', 'Prezinta Mici Defecte'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, null=True, blank=True)
    slug = models.SlugField()
    description = models.TextField()

    # Images
    image = models.ImageField()
    image_fata = models.ImageField(null=True, blank=True)
    image_interior = models.ImageField(null=True, blank=True)
    image_lateral1 = models.ImageField(null=True, blank=True)
    image_lateral2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

class SellWIthUsTwo(models.Model):
    full_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    stare = models.CharField(choices=STARE_CHOICES, max_length=30, null=True, blank=True)
    pret = models.IntegerField()
    image = models.ImageField(null=True)
    image_2 = models.ImageField(null=True)
    image_3 = models.ImageField(null=True)
    image_4 = models.ImageField(null=True) 
    image_5 = models.ImageField(null=True)

    def __str__(self):
        return self.full_name
    

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code

class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"

def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__():
        return f"{self.first_name} {self.last_name}"

class Terms(models.Model):
    title_terms = models.CharField(max_length=250)
    content_terms = models.TextField(null=True)
    definitii = models.TextField(null=True) 
    dispozitii_generale = models.TextField(null=True) 
    reguli_de_utilizare = models.TextField(null=True) 
    proprietate_intelectuala = models.TextField(null=True) 
    informatiile_prezentate = models.TextField(null=True) 
    politica_de_vanzare = models.TextField(null=True) 
    contul = models.TextField(null=True) 
    comanda = models.TextField(null=True) 
    livrarea = models.TextField(null=True) 
    transferul_proprietatii= models.TextField(null=True) 
    facturare_plata = models.TextField(null=True) 
    conformitatea_produselor = models.TextField(null=True) 
    dreptu_denuntare = models.TextField(null=True) 
    gdpr = models.TextField(null=True) 
    promovare_produse_si_oferte = models.TextField(null=True) 
    raspundere = models.TextField(null=True) 
    sesizari = models.TextField(null=True) 
    ultima_legislatie = models.TextField(null=True) 

    def __str__(self):
        return self.title_terms

    class Meta:
        verbose_name_plural = 'Terms'


class Privacy(models.Model):
    title_privacy = models.CharField(max_length=250)
    content_privacy = models.TextField(null=True)

class Refunds(models.Model):
    title_refunds = models.CharField(max_length=250)
    content_refunds = models.TextField(null=True)

class SellWithUs(models.Model):
    item_title = models.CharField(max_length=250)
    item_description = models.TextField()

class Gallery(models.Model):
    gallery_title = models.CharField(max_length=250)

class ThankYou(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

