from django import forms

class SearchForm(forms.Form):
    CITY_CHOICES = [
        ('', 'Shaharni tanlang'),
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
        ('', 'Turini tanlang'),
        ('HOVLI', 'Hovli'),
        ('KOTTEJ', 'Kottej'),
        ('TOMORQA', 'Tomorqa'),
        ('KVARTIRA', 'Kvartira'),
    ]

    city = forms.ChoiceField(choices=CITY_CHOICES, required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    price = forms.IntegerField(required=False)


    # bedrooms_num = forms.IntegerField(required=False)
    # bathrooms_num = forms.IntegerField(required=False)
    # garage_num = forms.IntegerField(required=False)
    # area_size = forms.IntegerField(required=False)



