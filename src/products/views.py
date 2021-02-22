from django.shortcuts import render
from .models import Product
from .forms import  RawProductForm, ProductForm
from django.http import HttpResponseRedirect
# Create your views here.


def product_detail_view (request, *args, **kwargs):
	obj =[] 
	products_iterator=Product.objects.all()
	for ids in products_iterator.iterator() :
		obj.append(ids)
		#obj.append(Product.objects.get(id=ids))

	product_context= {
		"obj":obj
	}
	return render (request, 'products.html', product_context)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
		return HttpResponseRedirect('../congrats')
	context= {
		"form":form
	}
	return render(request, "product/forms.html", context)
def congrats_view(request, *args,**kwargs):

	return render(request, 'product/congrats.html',{})
	
