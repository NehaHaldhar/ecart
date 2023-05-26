from django.db import models

class Maincategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    pic = models.ImageField(upload_to="subcategory",default=None, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="brands",default=None, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    maincategory = models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    baseprice = models.FloatField()
    discount = models.FloatField()
    finalprice = models.FloatField()
    stock = models.BooleanField(default=True)
    description = models.TextField()
    pic1 = models.ImageField(upload_to="products")
    pic2 = models.ImageField(upload_to="products",default=None, null=True, blank=True)
    pic3 = models.ImageField(upload_to="products", default=None, null=True, blank=True)
    pic4 = models.ImageField(upload_to="products", default=None, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    addressline1 = models.CharField(max_length=100,default="",null=True,blank=True)
    addressline2 = models.CharField(max_length=100,default="",null=True,blank=True)
    addressline3 = models.CharField(max_length=100,default="",null=True,blank=True)
    pin = models.CharField(max_length=10,default="",null=True,blank=True)
    city = models.CharField(max_length=30,default="",null=True,blank=True)
    state = models.CharField(max_length=30,default="",null=True,blank=True)
    pic = models.ImageField(upload_to="buyers",default="",null=True,blank=True)
    otp = models.IntegerField(default=100000)
    
    def __str__(self):
        return self.name+"/"+self.email
        

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    
    def __str__(self):
        return str(self.id)+" "+self.buyer.username+" "+self.product.name
         
 
paymentModes = ((1,"Cash on Delivery"),(2,"Net Banking"))
paymentStatus =((1,"Pending"),(2,"Done"))
orderStatus = ((1,"Order Placed"),(2,"Ready To Dispatch"),(3,"Dispatched"),(4,"Out For Delivery"),(5,"Delivered"))   
class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    paymentMode = models.IntegerField(choices=paymentModes,default=1)
    paymentStatus = models.IntegerField(choices=paymentStatus,default=1)
    orderStatus = models.IntegerField(choices=orderStatus,default=1)
    subtotal = models.IntegerField()
    shipping = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    rppid = models.CharField(max_length=30,default="")
    
    def __str__(self):
        return "Order ID : "+str(self.id)+" / Buyer Name: "+self.buyer.username
    

class OrderedProduct(models.Model):
    id = models.AutoField(primary_key=True)
    orderDetails = models.ForeignKey(OrderDetail,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return "Ordered Product ID :"+str(self.id)+" / Product ID :"+str(self.product.id)+" / "+self.product.name
    
# class DeliveryAddress(models.Model):
#     id = models.AutoField(primary_key=True)
#     orderDetail = models.ForeignKey(OrderDetail,on_delete=models.CASCADE)
#     receiver_name = models.CharField(max_length=40)
#     contact = models.CharField(max_length=15)
#     pincode = models.CharField(max_length=10)
#     address = models.CharField(max_length=60)
#     locality_town = models.CharField(max_length=20)
#     city_district = models.CharField(max_length=20)
#     state = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.person_name + self.contact
  
contactStatus = ((1,"Active"),(2,"Done"))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.IntegerField(choices=contactStatus,default=1)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" / "+self.name+" "+self.subject