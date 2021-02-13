from django.views import generic
from .models import Category
from .forms import SignUpForm
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login, authenticate
# Create your views here.

class ProductListView(generic.ListView):
    model = 'Category'
    queryset=Category.objects.all()
    template_name = 'index.html'

class ProductDetailView(generic.DetailView):
    model = 'Category'
    template_name = 'detail.html'

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})