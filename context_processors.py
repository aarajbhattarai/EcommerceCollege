from Product.models import Category

def category(request):
    category=Category.objects.all()
    return {'category':category}