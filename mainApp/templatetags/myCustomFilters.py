from django import template

register = template.Library()

@register.filter(name="paymentModeFilter")
def paymentModeFilter(Request,status):
    if(status==1):
        return "Cash on Delivey"
    else:
        return "Net Banking"

@register.filter(name="paymentStatusFilter")
def paymentStatusFilter(Request,status):
    if(status==1):
        return "Pending"
    else:
        return "Done"
   
@register.filter(name="orderStatusFilter")
def orderStatusFilter(Request,status):
    if(status==1):
        return "Order Placed"
    elif(status==2):
        return "Ready To Dispatch"
    elif(status==3):
        return "Dispatched"
    elif(status==3):
        return "Out For Delivery"
    else:
        return "Delivered"

@register.filter(name="payAgainFilter")
def payAgainFilter(Request, order):
    if(order.paymentStatus==1 and order.paymentMode==2):
        return True
    else:
        return False