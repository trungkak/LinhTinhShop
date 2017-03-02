
from .models import Product

def session_url(request):
    sess = request.session.get('cart',[])

    num = len(sess)

    attrs = []

    for item in sess:
    	object_attr = getattr(Product.objects.get(pk=item), 'name')
    	attrs.append(object_attr)

    return {'num_items':num, 'attrs': attrs}




