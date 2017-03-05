
from .models import Product

def session_url(request):
    sess = request.session.get('cart',[])

    num = len(sess)

    objs = []

    for item in sess:
    	obj = Product.objects.get(pk=item)
    	objs.append(obj)


    return {'num_items':num, 'objs': objs}




