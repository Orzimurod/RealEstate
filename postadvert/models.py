from django.db import models



class postadvert(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='advert/')
    posted_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
