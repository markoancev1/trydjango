from django.shortcuts import render, get_object_or_404, redirect

from django.http import Http404

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
    context = {
        'form': my_form
    }
    return render(request, 'product/product_create.html', context)

    # form = ProductForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #
    # context = {
    #     'form': form
    # }
    # return render(request, 'product/product_create.html', context)


def product_detail_view(request):

    obj = Product.objects.filter(id=1).first()
    context = {
        'object': obj,
    }
    return render(request, "product/detail.html", context)


def dynamic_lookup_view(request, id):

    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', context)


def product_delete_view(request, id):

    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }

    return render(request, 'product/delete.html', context)
