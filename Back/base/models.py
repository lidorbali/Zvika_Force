from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    
    
class Category(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    desc = models.TextField()
   
    
    def __str__(self):
        return self.desc   


# class Category(models.Modmel):
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

#     parent = models.ForeignKey(
#         'self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
#     name = models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return self.name












class Product(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    cat_id =models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    

class Order_det(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    order_id =models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    prod_id =models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    amount= models.IntegerField()
    total = models.IntegerField()

