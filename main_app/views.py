from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Store


# ---------------- STATIC
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



# ------------------- STORES
@login_required
def user_stores(request):
    stores = Store.objects.filter(user=request.user)
    context = {
        'stores': stores
    }
    return render(request, 'stores/user_index.html', context)


def stores_index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

def store_detail(request, store_id):
    store = Store.objects.get(id=store_id)
    all_candy = Candy.objects.filter(seller=store.id)

    context = {
        'store': store,
        'all_candy': all_candy,
    }
    return render(request, 'stores/detail.html', context)



@login_required
def new_store(request):
    if request.method == 'POST':
        store_form = StoreForm(request.POST)
        if store_form.is_valid():
            new_store = store_form.save(commit=False)
            new_store.user = request.user
            new_store.save()
            return redirect('store_detail', new_store.id)
    else:
        store_form = StoreForm()
        context = {
            'store_form': store_form
        }
        return render(request, 'stores/new.html', context)



# ------------------- PROFILE/USER
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_stores')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)

