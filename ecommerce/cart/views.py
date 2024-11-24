from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from cart.models import Cart,Payment,Order_details
from django.contrib.auth import login
from shop.models import Product
from django.contrib.auth.models import User
import razorpay


@login_required
def add_to_cart(request,i):
    p=Product.objects.get(id=i)
    u=request.user
    try:
        c=Cart.objects.get(user=u,product=p)#checks the proauct present in Cart for a particular user
        c.quantity+=1                       #if present it increment the quantity of product
        c.save()
        p.stock-=1
        p.save()
    except:                                 #if not present then it wilt create a new record inside cart table with quantity-1
        if(p.stock>0):
            c=Cart.objects.create(product=p,user=u,quantity=1)
            c.save()
            p.stock -= 1
            p.save()

    return redirect('cart:cartview')

@login_required
def cart_view(request):
    u=request.user
    total = 0
    c = Cart.objects.filter(user=u)
    for i in c:
        total += i.quantity * i.product.price
    context={'cart':c,'total': total}
    return render(request,'cart.html',context)

@login_required
def cart_remove(request,i):
    p=Product.objects.get(id=i)
    u=request.user

    try:
        c=Cart.objects.get(user=u,product=p)
        if(c.quantity>1):
            c.quantity-=1
            c.save()
            p.stock+=1
            p.save()
        else:
            c.delete()
            p.stock+=1
            p.save()

    except:
        pass

    return redirect('cart:cartview')

@login_required
def cart_delete(request,i):
    u = request.user
    p = Product.objects.get(id=i)

    try:
        c=Cart.objects.get(user=u, product=p)
        p.stock += c.quantity
        p.save()
        c.delete()

    except:
        pass

    return redirect('cart:cartview')

def order_form(request):
    if(request.method=="POST"):
        address=request.POST['a']
        pin = request.POST['pi']
        phone = request.POST['p']

        u=request.user

        c=Cart.objects.filter(user=u)
        total=0
        for i in c:
            total+=i.quantity*i.product.price
        total=int(total*100)
        client=razorpay.Client(auth=('rzp_test_vgB2UPL8zEzdCu','a0aMvBuzOfhLJVUZjC7eJTuv')) #client connection using id and secret code of razorpay
        response_payment=client.order.create(dict(amount=total,currency="INR"))#creates an order with razorpay client
        # print(response_payment)
        order_id=response_payment['id']
        order_status = response_payment['status']
        if(order_status=='created'):
            p=Payment.objects.create(name=u.username,amount=total,order_id=order_id)
            p.save()
            for i in c:
                c=Order_details.objects.create(product=i.product,user=u,no_of_items=i.quantity,address=address,pin=pin,phone_no=phone,order_id=order_id)
                c.save()
            else:
                pass
            response_payment['name']=u.username
            context={'payment':response_payment}
            return render(request,'payment.html',context)
    return render(request,'orderform.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def payment_status(request,u):
    user = User.objects.get(username=u)
    if(not request.user.is_authenticated):
        login(request,user)
    if(request.method=="POST"):
        response=request.POST
        print(response)
        print(u)
        param_dict={
            'razorpay_order_id':response['razorpay_order_id'],
            'razorpay_payment_id':response['razorpay_payment_id'],
            'razorpay_signature':response['razorpay_signature'],
        }

        client=razorpay.Client(auth=('rzp_test_vgB2UPL8zEzdCu','a0aMvBuzOfhLJVUZjC7eJTuv'))
        print(client)
        try:
            status=client.utility.verify_payment_signature(param_dict)
            print(status)
            #to retrive a perticular record in payment table whose order id matches the response order id
            p=Payment.objects.get(order_id=response['razorpay_order_id'])
            p.razorpay_payment_id=response['razorpay_payment_id'] #adds the payment id after successful payment
            p.paid=True#changes th epaid status to true
            p.save()



            o=Order_details.objects.filter(user=user,order_id=response['razorpay_order_id'])
            for i in o:
                i.payment_status="paid"
                i.save()

            c=Cart.objects.filter(user=user)
            c.delete()
        except:
            print("theres an error")
    return render(request,'payment_status.html',{'status':status})

@login_required
def order_view(request):
    u=request.user
    o=Order_details.objects.filter(user=u,payment_status="paid")
    context={'order':o}
    return render(request, 'order_view.html', context)