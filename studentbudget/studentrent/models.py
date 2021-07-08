from django.db import models


# Create your models here.
class renthouse(models.Model):
    
    housetype = models.CharField(max_length=100)
    slug =models.SlugField(max_length=250, blank=True,null=True)
    room = models.IntegerField()
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    available = models.DateTimeField()
    img= models.ImageField(upload_to='pics')
    disc=models.TextField()
    post_date= models.DateTimeField(auto_now="True")
    
class favorite_house(models.Model):
    favorite_house = models.ForeignKey(renthouse, on_delete=models.CASCADE)
    def __str__(self):
        return "Favorite House:"+str(self.id)

class housebooking(models.Model):
    renthouseid = models.CharField(max_length=100)
    renter_name = models.CharField(max_length=100)
    cardholder_name=models.CharField(max_length=100)
    cardnumber= models.CharField(max_length=100)
    expiry_date=models.DateField()
    cvc=models.CharField(max_length=3)
    email=models.EmailField()

    