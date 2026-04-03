# ...existing code...
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, User
from .forms import UserForm

def home(request):
    # use the app namespace to avoid ambiguity when included with a namespace
    return redirect('cafeteria_app:user_list')

def product_list(request):
    """Vue qui fournit la liste des produits au template product_list.html"""
    products = Product.objects.filter(available=True).order_by('name')
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    """Exemple d'utilisation d'un paramètre d'URL et de request"""
    product = get_object_or_404(Product, pk=pk)
    apply_discount = request.GET.get('discount') == '1'
    return render(request, 'product_detail.html', {'product': product, 'apply_discount': apply_discount})

# CRUD pour les utilisateurs
def user_list(request):
    users = User.objects.order_by('name')
    return render(request, 'user_list.html', {'users': users})

def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafeteria_app:user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form, 'action': 'Ajouter'})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('cafeteria_app:user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form, 'action': 'Modifier'})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('cafeteria_app:user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})
# ...existing code...
