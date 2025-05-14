from django.db import models


class Slides(models.Model):
    image = models.ImageField(upload_to='slides/')
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Listing(models.Model):
    CITY_CHOICES = [
        ('TOSHKENT', 'Toshkent'),
        ('SIRDARYO', 'Sirdaryo'),
        ('SAMARQAND', 'Samarqand'),
        ('ANDIJON', 'Andijon'),
        ('FARGONA', 'Fargona'),
        ('JIZZAX', 'Jizzax'),
        ('NAVOIY', 'Navoiy'),
        ('SURXONDARYO', 'Surxondaryo'),
        ('QASHQADARYO', 'Qashqadaryo'),
        ('XORAZM', 'Xorazm'),
        ('QORAQALPOGISTON', 'Qoraqalpogiston'), 
        ('BUXORO', 'Buxoro'),
        ('NAMANGAN', 'Namangan'),
    ]

    CATEGORY_CHOICES = [
        ('HOVLI', 'Hovli'),
        ('KOTTEJ', 'Kottej'),
        ('TOMORQA', 'Tomorqa'),
        ('KVARTIRA', 'Kvartira'),
    ]

    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='listings/')
    posted_at = models.DateTimeField(auto_now_add=True)
    bedrooms_num = models.IntegerField(blank=True, null=True)
    bathrooms_num = models.IntegerField(blank=True, null=True)
    garage_num = models.IntegerField(blank=True, null=True)
    area_size = models.IntegerField(blank=True, null=True)
    area_size = models.IntegerField()
    is_approved = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title


class advert(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='advert/')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class founder(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='founder/')
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

