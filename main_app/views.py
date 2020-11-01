from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Store, Candy
from .forms import StoreForm, CandyForm


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

@login_required
def stores_index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

@login_required
def store_detail(request, store_id):
    store = Store.objects.get(id=store_id)
    all_candy = Candy.objects.filter(store=store.id)

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


@login_required
def delete_store(request, store_id):
    Store.objects.get(id=store_id).delete()
    return redirect('user_stores')


@login_required
def edit_store(request, store_id):
    store = Store.objects.get(id=store_id)
    if request.method == 'POST':
        store_form = StoreForm(request.POST, instance=store)
        if store_form.is_valid():
            updated_store = store_form.save()
            return redirect('user_stores')
    else:
        store_form = StoreForm(instance=store)
        context = {
            'store_form': store_form
        }
        return render(request, 'stores/edit.html', context)



# ------------------- CANDY
def candy_index(request):
    all_candy = Candy.objects.all()
    context = {
        'all_candy': all_candy
    }
    return render(request, 'candy/index.html', context)


@login_required
def candy_detail(request,candy_id):
    candy = Candy.objects.get(id=candy_id)
    store = candy.store.id
    context = {
        'candy': candy,
        'store': store
    }
    return render(request, 'candy/detail.html', context)


@login_required
def add_candy(request, store_id):
    store = Store.objects.get(id=store_id)
    if request.method == 'POST':
        candy_form = CandyForm(request.POST)
        if candy_form.is_valid():
            new_form = candy_form.save(commit=False)
            new_form.store_id = store_id
            new_form.save()
            return redirect('store_detail', store_id)
    else:
        candy_form = CandyForm()
        context = {
            'store': store,
            'candy_form': candy_form
        }
        return render(request, 'candy/new.html', context)
 

@login_required
def edit_candy(request, candy_id):
    candy = Candy.objects.get(id=candy_id)
    if request.method == 'POST':
        candy_form = CandyForm(request.POST, instance=candy)
        if candy_form.is_valid():
            updated_candy = candy_form.save()
            return redirect('candy_detail', updated_candy.id)
    else:
        candy_form = CandyForm()
        context = {
            'candy_form': candy_form,
            'candy': candy
        }
        return render(request, 'candy/edit.html', context)


@login_required
# def delete_candy(request, store_id, candy_id):
def delete_candy(request, candy_id):
    candy = Candy.objects.get(id=candy_id)
    store = candy.store.id
    candy.delete()
    # Candy.objects.get(id=candy_id).delete()
    return redirect('store_detail', store)


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

