from cart.models import Cart
def cartitems(request):
    icount=0
    if request.user:
        u=request.user
        try:
            c=Cart.objects.filter(user=u)
            for i in c:
                icount+=i.quantity
        except:
            icount=0
    return {'count':icount}