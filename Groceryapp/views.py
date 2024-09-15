from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
#accessing our models so we can get content from them
from Groceryapp.models import *   #it means from Groceryapp, in the models.py file, import all
#borrowing decorators from django to restrict access to my pages
from django.contrib.auth.decorators import login_required
#importing a response to delete
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import SaleForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from .filters import StockFilter
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CreditSale
from .forms import CreditSaleForm


# Create your views here.
def index(request):
    items = Stock.objects.all().order_by('-id')
    return render(request,'Groceryapp/index.html', {'items': items})


@login_required
def home(request):
    products = Stock.objects.all().order_by('-id') #we're creating a variable called stock, arranged by their orders called ids
    #applying filters to a query set
    product_filters = StockFilter(request.GET, queryset=products)
    products = product_filters.qs
    return render(request, 'Groceryapp/home.html', {'products': products, 'product_filters': product_filters})

@login_required
def product_detail(request,product_id):
    product = Stock.objects.get(id = product_id)
    return render(request,'Groceryapp/product_detail.html',{'product':product})

@login_required
def delete_detail(request,product_id):
    product = Stock.objects.get(id = product_id)
    product.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required
def issue_item(request,pk):
    #accessing all objects from the stock model
    issued_item = Stock.objects.get(id=pk)
    #accessing our form
    sales_form = SaleForm(request.POST)
    #receiving data from the form and saving it in the model
    if request.method == 'POST':
    #checking whether the form is valid
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #keep track of stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.stock_quantity -= issued_quantity
            issued_item.save()
        return redirect('receipt')
    return render(request,'Groceryapp/issue_item.html', {'sales_form': sales_form})

@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'Groceryapp/receipt.html', {'sales': sales})

@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'Groceryapp/receipt_detail.html', {'receipt': receipt})

@login_required
def loginout(request):
    return render(request, 'Groceryapp/logout.html')


@login_required
def manage_credit(request, credit_sale_id=None):
    if credit_sale_id:
        credit_sale = get_object_or_404(CreditSale, id=credit_sale_id)
    else:
        credit_sale = None

    if request.method == 'POST':
        form = CreditSaleForm(request.POST, instance=credit_sale)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreditSaleForm(instance=credit_sale)

    return render(request, 'Groceryapp/manage_credit.html', {'form': form, 'credit_sale': credit_sale})

@login_required
def delete_credit_sale(request, credit_sale_id):
    credit_sale = get_object_or_404(CreditSale, id=credit_sale_id)
    credit_sale.delete()
    return redirect('home')