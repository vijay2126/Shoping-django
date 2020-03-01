from django.db import models

# Create your models here.
class User1(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    number = models.CharField(max_length=10)



class RegisterModel(models.Model):
    First_name =models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    email =models.EmailField()
    mobile_no=models.CharField(max_length=10)
    Addresh=models.CharField(max_length=100)







class RegisterModel1(models.Model):
    First_name =models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    email =models.EmailField()
    mobile_no=models.CharField(max_length=10)
    Addresh=models.CharField(max_length=100)
    Password1=models.CharField(max_length=25)




class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name

