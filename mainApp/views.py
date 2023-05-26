from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from ecart.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay

import socket
socket.getaddrinfo('yourhostname.com', 80)


def home(Request):
    product = Product.objects.all().order_by("-id")[0:12]
    maincategory = Maincategory.objects.all()
    brands = Brand.objects.all()
    subcategory = Subcategory.objects.all()
    data = []
    for item in maincategory:
        data.append(item.name)
    Request.session['maincategory'] = data
    data = []
    for item in subcategory:
        data.append(item.name)
    Request.session['subcategory'] = data
    data = []
    for item in brands:
        data.append(item.name)
    Request.session['brand'] = data
    
    return render(Request, 'index.html', {"product": product,"subcategory":subcategory,"brands":brands})


def shop(Request, mc, sc, br):
    if (mc == "All" and sc == "All" and br == "All"):
        data = Product.objects.all().order_by("-id")
    elif (mc != "All" and sc == "All" and br == "All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-id")
    elif (mc == "All" and sc != "All" and br == "All"):
        data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
    elif (mc == "All" and sc == "All" and br != "All"):
        data = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("-id")
    elif (mc != "All" and sc != "All" and br == "All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
    elif (mc == "All" and sc != "All" and br != "All"):
        data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br)).order_by("-id")
    elif (mc != "All" and sc == "All" and br != "All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), brand=Brand.objects.get(name=br)).order_by("-id")
    else:
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br)).order_by("-id")

    maincategories = Maincategory.objects.all()
    subcategories = Subcategory.objects.all()
    brands = Brand.objects.all()
    return render(Request, 'shop.html', {"data": data, "maincategories": maincategories, "subcategories": subcategories, "brands": brands, "mc": mc, "sc": sc, "br": br})


def priceSortFilter(Request, mc, sc, br, filter):
    if (filter == "Latest"):
        if (mc == "All" and sc == "All" and br == "All"):
            data = Product.objects.all().order_by("-id")
        elif (mc != "All" and sc == "All" and br == "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-id")
        elif (mc == "All" and sc != "All" and br == "All"):
            data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
        elif (mc == "All" and sc == "All" and br != "All"):
            data = Product.objects.filter(  brand=Brand.objects.get(name=br)).order_by("-id")
        elif (mc != "All" and sc != "All" and br == "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
        elif (mc == "All" and sc != "All" and br != "All"):
            data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br)).order_by("-id")
        elif (mc != "All" and sc == "All" and br != "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), brands=Brand.objects.get(name=br)).order_by("-id")
        else:
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br)).order_by("-id")
    elif (filter == "LTH"):
        if (mc == "All" and sc == "All" and br == "All"):
            data = Product.objects.all().order_by("finalprice")
        elif (mc != "All" and sc == "All" and br == "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("finalprice")
        elif (mc == "All" and sc != "All" and br == "All"):
            data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("finalprice")
        elif (mc == "All" and sc == "All" and br != "All"):
            data = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("finalprice")
        elif (mc != "All" and sc != "All" and br == "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc)).order_by("finalprice")
        elif (mc == "All" and sc != "All" and br != "All"):
            data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br)).order_by("finalprice")
        elif (mc != "All" and sc == "All" and br != "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), brands=Brand.objects.get(name=br)).order_by("finalprice")
        else:
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br)).order_by("finalprice")
    else:
        if (mc == "All" and sc == "All" and br == "All"):
            data = Product.objects.all().order_by("-finalprice")
        elif (mc != "All" and sc == "All" and br == "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-finalprice")
        elif (mc == "All" and sc != "All" and br == "All"):
            data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-finalprice")
        elif (mc == "All" and sc == "All" and br != "All"):
            data = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("-finalprice")
        elif (mc != "All" and sc != "All" and br == "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc)).order_by("-finalprice")
        elif (mc == "All" and sc != "All" and br != "All"):
            data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br)).order_by("-finalprice")
        elif (mc != "All" and sc == "All" and br != "All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get( name=mc), brands=Brand.objects.get(name=br)).order_by("-finalprice")
        else:
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br)).order_by("-finalprice")

    maincategories = Maincategory.objects.all()
    subcategories = Subcategory.objects.all()
    brands = Brand.objects.all()
    return render(Request, 'shop.html', {"data": data, "maincategories": maincategories, "subcategories": subcategories, "brands": brands, "mc": mc, "sc": sc, "br": br, "filter": filter})

def priceRangeFilter(Request, mc, sc, br):
    option = Request.POST.get("price")
    if(option == "1"):
        min = 0
        max = 1000000000
    elif(option == "2"):
        min = 0
        max = 1000
    elif(option == "3"):
        min = 1000
        max = 2000
    elif(option == "4"):
        min = 2000
        max = 3000 
    elif(option == "5"):
        min = 3000
        max = 4000
    elif(option == "6"):
        min = 4000
        max = 5000
    elif(option == "7"):
        min = 5000
        max = 1000000000       
        
        
    if (mc == "All" and sc == "All" and br == "All"):
        data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max).order_by("-id")
    elif (mc != "All" and sc == "All" and br == "All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),finalprice__gte=min,finalprice__lte=max).order_by("-id")
    elif (mc == "All" and sc != "All" and br == "All"):
        data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc),finalprice__gte=min,finalprice__lte=max).order_by("-id")
    elif (mc == "All" and sc == "All" and br != "All"):
        data = Product.objects.filter(brand=Brand.objects.get(name=br),finalprice__gte=min,finalprice__lte=max).order_by("-id")
    elif (mc != "All" and sc != "All" and br == "All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc),finalprice__gte=min,finalprice__lte=max).order_by("-id")
    elif (mc == "All" and sc != "All" and br != "All"):
        data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br),finalprice__gte=min,finalprice__lte=max).order_by("-id")
    elif (mc != "All" and sc == "All" and br != "All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get( name=mc), brands=Brand.objects.get(name=br),finalprice__gte=min,finalprice__lte=max).order_by("-id")
    else:
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc), brand=Brand.objects.get(name=br),finalprice__gte=min,finalprice__lte=max).order_by("-id")

    maincategories = Maincategory.objects.all()
    subcategories = Subcategory.objects.all()
    brands = Brand.objects.all()
    return render(Request, 'shop.html', {"data": data, "maincategories": maincategories, "subcategories": subcategories, "brands": brands, "mc": mc, "sc": sc, "br": br})

def search(Request):
    if(Request.method=="POST"):
        search = Request.POST.get("search")
        data = Product.objects.filter( Q(name__contains = search) | Q(color__contains = search) | Q(size__contains = search) | Q(description__contains = search) | Q(finalprice__contains = search))
        maincategories = Maincategory.objects.all()
        subcategories = Subcategory.objects.all()
        brands = Brand.objects.all()
        return render(Request, 'shop.html', {"data": data, "maincategories": maincategories, "subcategories": subcategories, "brands": brands, "mc": "All", "sc": "All", "br": "All"})
    else:
        return HttpResponseRedirect("/")
    
def singleProduct(Request, id):
    product = Product.objects.get(id=id)
    relatedProducts = Product.objects.filter(maincategory = Maincategory.objects.get(name = product.maincategory),subcategory = Subcategory.objects.get(name = product.subcategory))
    return render(Request, 'single-product.html',{"product":product,"relatedProducts":relatedProducts})

def login(Request):
    if(Request.method == "POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        
        user = auth.authenticate(username=username,password=password)
        if (user is None):
            messages.error(Request,"Invalid Username or password!!!")
        else:
            auth.login(Request,user)
            if (user.is_superuser):
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/profile/")
    return render(Request, 'login.html')


def signUp(Request):
    if(Request.method=="POST"):
        if(Request.POST.get("password")!=Request.POST.get("cpassword")):
            messages.error(Request,"password and confirm password are not same")
        else:
            try:
                user = User.objects.create(username=Request.POST.get("username"))
                user.set_password(Request.POST.get("password"))
                user.save()
                
                b = Buyer()
                b.name = Request.POST.get("name")
                b.username = user
                b.email = Request.POST.get("email")
                b.phone = Request.POST.get("phone")
                b.save()

                subject = 'Account Created Successfully : Team E-Cart'
                message = f'''Hi {user.username},
                        Thanks to create an Account with us
                        Now you can Buy Latest Products.
                        Your account comes with access to E-Cart services.
                        Team E-Cart
                        '''
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [b.email, ]
                send_mail( subject, message, email_from, recipient_list )
                
                messages.success(Request,"Account Created Successfully :)")
                return HttpResponseRedirect("/login/")
            except:
                messages.error(Request,"Username already Exist")   
    return render(Request, 'signup.html')

@login_required(login_url="/login/")
def profile(Request):
    user = User.objects.get(username=Request.user.username)
    if user.is_superuser:
        return HttpResponseRedirect("/admin/")
    else:
        buyer = Buyer.objects.get(username = Request.user.username)
        
        od = OrderDetail.objects.filter(buyer=buyer).order_by("-id")
        orders = []
        for item in od:
            op = OrderedProduct.objects.filter(orderDetails=item.id)
            orders.append({'orderDetail':item,'orderedProducts':op})
        return render(Request,"profile.html",{"data":buyer,'orders':orders})
    
@login_required(login_url="/login/")
def update(Request):
    user = User.objects.get(username=Request.user.username)
    if user.is_superuser:
        return HttpResponseRedirect("/admin/")
    else:
        buyer = Buyer.objects.get(username = Request.user.username)
        if(Request.method == "POST"):
            buyer.name = Request.POST.get("name")
            buyer.email = Request.POST.get("email")
            buyer.phone = Request.POST.get("phone")
            buyer.addressline1 = Request.POST.get("addressline1")
            buyer.addressline2 = Request.POST.get("addressline2")
            buyer.addressline3 = Request.POST.get("addressline3")
            buyer.pin = Request.POST.get("pin")
            buyer.city = Request.POST.get("city")
            buyer.state = Request.POST.get("state")
            if(Request.FILES.get("pic")!=""):
                buyer.pic = Request.FILES.get("pic")
            buyer.save()
            return HttpResponseRedirect("/profile/")
        return render(Request,"update-profile.html",{"data":buyer})
    

def logout(Request):
    auth.logout(Request)
    return HttpResponseRedirect("/login/")

@login_required(login_url="/login/")
def add_to_cart(Request,num):
    p = Product.objects.get(id=num)
    if(p):
        cart = Request.session.get("cart",None)
        if(cart):
            if(str(num) in cart):
                return HttpResponseRedirect("/cart/")
            else:
                cart.setdefault(str(num),{'id':p.id,'name':p.name,'brand':p.brand.name,'color':p.color,'size':p.size,'price':p.finalprice,'qty':1,'total':p.finalprice,'pic':p.pic1.url})
        else:
            cart = {str(num):{'id':p.id,'name':p.name,'brand':p.brand.name,'color':p.color,'size':p.size,'price':p.finalprice,'qty':1,'total':p.finalprice,'pic':p.pic1.url}}
        subtotal = 0
        count = 0
        for key,values in cart.items():
            subtotal = subtotal+values['total']
            count = count + values['qty']
        if(subtotal>0 and subtotal<10000):
            shipping = 150
        else:
            shipping =  0
        total = subtotal + shipping
        Request.session['cart']=cart        
        Request.session['subtotal']=subtotal        
        Request.session['shipping']=shipping        
        Request.session['total']=total        
        Request.session['count']=count        
        Request.session.set_expiry(60*60*24*30)
        return HttpResponseRedirect("/cart/")
    else:
        return HttpResponseRedirect("/shop/All/All/All")

@login_required(login_url="/login/")
def cart(Request):
    cart = Request.session.get("cart",None)
    return render(Request, 'cart.html',{'cart':cart})

def remove_cart_item(Request,num):
    cart = Request.session.get("cart",None)
    if(cart and num in cart):
        del cart[num]
        Request.session.get("cart",None)
        subtotal = 0
        count = 0
        for key,values in cart.items():
            subtotal = subtotal+values['total']
            count = count + values['qty']
        if(subtotal>0 and subtotal<10000):
            shipping = 150
        else:
            shipping =  0
        total = subtotal + shipping
        Request.session['cart']=cart        
        Request.session['subtotal']=subtotal        
        Request.session['shipping']=shipping        
        Request.session['total']=total        
        Request.session['count']=count    
    return HttpResponseRedirect("/cart/")    

def update_cart_page(Request,num,op):
    cart = Request.session.get("cart",None)
    if(cart and num in cart):
        item = cart[num]
        if(item['qty'] == 1 and op=='dec'):
            pass
        elif(op=="dec"):
            item['qty'] = item['qty'] - 1
            item['total'] = item['total'] - item['price']
        else:
            item['qty'] = item['qty'] + 1
            item['total'] = item['total'] + item['price']   
        subtotal = 0
        count = 0
        for key,values in cart.items():
            subtotal = subtotal+values['total']
            count = count + values['qty']
        if(subtotal>0 and subtotal<10000):
            shipping = 150
        else:
            shipping =  0
        total = subtotal + shipping
        Request.session['cart']=cart        
        Request.session['subtotal']=subtotal        
        Request.session['shipping']=shipping        
        Request.session['total']=total        
        Request.session['count']=count
        Request.session.set_expiry(60*60*24*30)
    
    return HttpResponseRedirect("/cart/")

@login_required(login_url="/login/")
def add_to_wishlist(Request,num):
    try:
        p = Product.objects.get(id=num)
        b = Buyer.objects.get(username=Request.user.username)
        c= 0 
        try:
            wishlist = Wishlist.objects.get(buyer = b, product = p)
        except:
            w = Wishlist()
            w.buyer = b
            w.product = p
            w.save()
        Request.session['wish_count'] = c
    except:
        pass
    return HttpResponseRedirect("/wishlist/")

@login_required(login_url="/login/")
def remove_from_wishlist(Request,num):
    try:
        item = Wishlist.objects.get(id=num)
        item.delete()
    except:
        pass
    return HttpResponseRedirect("/wishlist/")

@login_required(login_url="/login/")   
def wishlist(Request):
    buyer = Buyer.objects.get(username = Request.user.username)
    wishlist = Wishlist.objects.filter(buyer=buyer)
    c = 0
    for w in wishlist:
            c = c+1
    Request.session['wish_count'] = c
    return render(Request,"wishlist.html",{"data":buyer,'wishlist':wishlist})

@login_required(login_url="/login/")     
def checkout(Request):
    try:
        buyer = Buyer.objects.get(username=Request.user.username)
        if(buyer.addressline1 == "" or buyer.pin == "" or buyer.city == "" or buyer.state == ""):
            return HttpResponseRedirect('/add-address/')
        else:
            return render(Request, 'checkout.html',{'buyer':buyer})
    except:
        return HttpResponseRedirect("/login/")
    
@login_required(login_url="/login/")
def add_address_page(Request):
    return render(Request,"add-address.html")

@login_required(login_url="/login/")
def update_address(Request):
    user = User.objects.get(username=Request.user.username)
    if user.is_superuser:
        return HttpResponseRedirect("/admin/")
    else:
        buyer = Buyer.objects.get(username = Request.user.username)
        if(Request.method == "POST"):
            buyer.addressline1 = Request.POST.get("addressline1")
            buyer.addressline2 = Request.POST.get("addressline2")
            buyer.addressline3 = Request.POST.get("addressline3")
            buyer.pin = Request.POST.get("pin")
            buyer.city = Request.POST.get("city")
            buyer.state = Request.POST.get("state")
            buyer.save()
        return render(Request, 'checkout.html',{'buyer':buyer})

client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
@login_required(login_url="/login/")    
def place_order(Request):
    if(Request.method=="POST"):
        buyer = Buyer.objects.get(username=Request.user.username)
        mode = Request.POST.get("mode")
        subtotal = Request.session.get("subtotal",0)
        shipping = Request.session.get("shipping",0)
        total = Request.session.get("total",0)
        if(subtotal==0):
            return HttpResponseRedirect("/cart/")
        print(mode)
        order_details = OrderDetail()
        
        order_details.buyer = buyer
        # order_details.paymentMode = mode
        order_details.subtotal = subtotal
        order_details.shipping = shipping
        order_details.total = total
        order_details.save()
        
        cart = Request.session.get("cart",None)
        for key,values in cart.items():
            
            cart_products = Product.objects.get(id=(int(key)))
            
            ordered_product = OrderedProduct()
            
            ordered_product.orderDetails = order_details    # object of OrderDetail(ForeignKey)
            ordered_product.product = cart_products
            ordered_product.qty = values['qty']
            ordered_product.total = values['total']
            ordered_product.save()
            
        Request.session['cart'] = {}
        Request.session['subtotal'] = 0
        Request.session['shipping'] = 0
        Request.session['total'] = 0
        Request.session['count'] = 0
        
        if(mode=="1"):
            subject = 'Order Has Been Placed : Team E-Cart'
            message = f'''Hello {buyer.username},
                        Your order has been Placed with order ID :{order_details.id}
                        Track your Order http://localhost:8000/profile/
                        '''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [buyer.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponseRedirect("/confirmation/")
        else:
            orderAmount = order_details.total*100
            orderCurrency = "INR"
            paymentOrder = client.order.create(dict(amount=orderAmount,currency=orderCurrency,payment_capture=1))
            paymentId = paymentOrder['id']
            order_details.paymentMode=2
            order_details.save()
            return render(Request,"pay.html",{
                "amount":orderAmount,
                "api_key":RAZORPAY_API_KEY,
                "order_id":paymentId,
                "User":buyer
            })
    else:
        return HttpResponseRedirect("/checkout/")
    
@login_required(login_url='/login/')
def paymentSuccessPage(Request,rppid,rpoid,rpsid):
    buyer = Buyer.objects.get(username=Request.user)
    od = OrderDetail.bjects.filter(user=buyer)
    od = od[::-1]
    od = od[0]
    od.rppid = rppid
    od.paymentStatus = 2
    od.save()
    
    subject = 'Order Has Been Placed : Team E-Cart'
    message = f'''Hello {buyer.username},
                Your order has been Placed with order ID :{od.id}
                Track your Order http://localhost:8000/profile/
                '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [buyer.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/confirmation/')
    

@login_required(login_url="/login/")
def confirmation(Request):
    return render(Request,"confirmation.html")

def contact(Request):
    if(Request.method=="POST"):
        c = Contact()
        c.name = Request.POST.get("name")
        c.email = Request.POST.get("email")
        c.phone = Request.POST.get("phone")
        c.subject = Request.POST.get("subject")
        c.message = Request.POST.get("message")
        c.save()
        
        messages.success(Request,"Thanks to Share Your Query With Us :) Our Team Will Contact You Soon!!!")
        
    return render(Request, 'contact.html')

def forget_password_1(Request):
    if(Request.method=="POST"):
        username = Request.POST.get("username")
        try:
            user = Buyer.objects.get(username=username)
            otp = randint(100000,999999)
            user.otp = otp
            user.save()
            
            subject = 'OTP for Password Reset : Team E-Cart'
            message = f'''Hi {user.username},
                        {otp} is your otp to reset password of your E-Cart Account.'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            
            messages.success(Request,"OTP has sent to registered mail")
            Request.session['reset-password-username'] = username            
            return HttpResponseRedirect("/forget-password-2/")
        except:     
            messages.warning(Request,"Invalid username")
    
    return render(Request,"forget-password-1.html")

def forget_password_2(Request):
    if(Request.method=="POST"):
        otp = int(Request.POST.get("otp"))
        try:
            user = Buyer.objects.get(username=Request.session.get("reset-password-username",None))
            if(otp==user.otp):
                return HttpResponseRedirect("/forget-password-3/")
            else:
                messages.warning(Request,"Invalid OTP!!!")
        except:
            messages.warning(Request,"Un-Authorized")
    return render(Request,"forget-password-2.html")

def forget_password_3(Request):
    if(Request.method=="POST"):
        new_pass = Request.POST.get("npassword")
        cpass = Request.POST.get("cpassword")
        if(new_pass==cpass):
            try:
                user = User.objects.get(username=Request.session.get("reset-password-username",None))
                user.set_password(new_pass)
                user.save()
                if(Request.session['reset-password-username']):
                    del Request.session['reset-password-username']
                messages.success(Request,"Password Changed Successfully")
                return HttpResponseRedirect("/login/")
            except:
                messages.warning(Request,"Un-Authorized")
        else:
            messages.warning(Request,"Passwords Does Not Mathes!!")
    return render(Request,"forget-password-3.html")

