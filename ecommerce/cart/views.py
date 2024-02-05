from django.shortcuts import render
from shop.models import Products
from cart.models import Cart,Account,Order
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def cartview(request):
    u=request.user
    c=Cart.objects.filter(user=u)
    total=0
    for i in c:
        total+=i.quantity*i.product.price
    # print(total)
    return render(request,'cart.html',{'c':c,'total':total})

@login_required
def cart(request,p):
    b=Products.objects.get(name=p)
    u=request.user
    try:
        c=Cart.objects.get(user=u,product=b)
        if(b.stock>0):
            c.quantity+=1
            c.save()
            b.stock-=1
            b.save()
    except:
        if(b.stock>0):
            c = Cart.objects.create(product=b, user=u, quantity=1)
            c.save()
            b.stock-=1
            b.save()
    return cartview(request)

@login_required
def deletecart(request,p):
    b = Products.objects.get(name=p)
    u = request.user
    try:
        c = Cart.objects.get(user=u,product=b)
        if(c.quantity>1):
            c.quantity -= 1
            c.save()
            b.stock += 1
            b.save()
        else:
            c.delete()
            b.stock += 1
            b.save()
    except:
        pass
    return cartview(request)

@login_required
def removecart(request,p):
    b=Products.objects.get(name=p)
    u=request.user
    try:
        c=Cart.objects.get(product=b,user=u)
        c.delete()
        b.stock += c.quantity
        b.save()
    except:
        pass
    return cartview(request)

@login_required
def orderform(request):
    if(request.method=='POST'):
        a=request.POST['a']
        p= request.POST['p']
        ac=request.POST['ac']

        u=request.user
        c=Cart.objects.filter(user=u)

        total = 0
        for i in c:
            total += i.quantity * i.product.price

        try:
            n=Account.objects.get(accntnum=ac)
            if(n.amount>=total):
                n.amount=n.amount-total
                n.save()

                for i in c:
                    o=Order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status='paid')
                    o.save()
                c.delete()
                msg="Your order placed successfully"
                return render(request,'orderdetail.html',{'msg':msg})
            else:
                msg='Insufficient amount.You cant Place order'
                return render(request,'orderdetail.html',{'msg':msg})
        except:
            pass

    return render(request,'orderform.html')

@login_required
def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u)
    return render(request,'orderview.html',{'order':o,'u':u})