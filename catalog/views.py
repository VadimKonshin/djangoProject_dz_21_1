from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category


def catalog(requests):
    return render(requests, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'contacts.html')


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
    }
    return render(request, 'product_list.html', context)


def catalog_products(request, pk):
    catalog_list = get_object_or_404(Category, pk=pk)
    contex = {
        'object_list': catalog_list,
    }
    return render(request, 'catalog_products.html', contex)
