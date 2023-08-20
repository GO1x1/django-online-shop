from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, ModelFormMixin, FormView, CreateView

from OnlineShop.forms import CreateUserForm
from OnlineShop.models import Product, Category_brands, Category_model, Category_for, Image, Order, Sex
from cart.forms import CartAddProductForm


def alltype(kwargs):
    kwargs['brands'] = Category_brands.objects.all()
    kwargs['section'] = Category_model.objects.all()
    kwargs['type'] = Category_for.objects.all()
    kwargs['sex'] = Sex.objects.all()
    return kwargs

def pagination_p(request, context, items):
    if 'page' in request.GET:
        page = request.GET['page']
    else:
        page = 1
    paginator = Paginator(items, 3)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context['items'] = items

def all_for_main_page():
    brands = Category_brands.objects.all()
    section = Category_model.objects.all()
    type = Category_for.objects.all()

    context = {'brands': brands, 'section': section, 'type': type}
    return context

class MainPage(ListView):
    model = Product
    template_name = 'OnlineShop/shop.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return alltype(context)

class MainPageSex(ListView):
    model = Product
    template_name = 'OnlineShop/shop.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return alltype(context)

    def get_queryset(self):
        return Product.objects.filter(sex__slug=self.kwargs['sex_slug'])

class MainPageBrand(ListView):
    model = Product
    template_name = 'OnlineShop/shop.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return alltype(context)

    def get_queryset(self):
        return Product.objects.filter(category_brands__slug=self.kwargs['category_brands_slug'])

class MainPageModel(ListView):
    model = Product
    template_name = 'OnlineShop/shop.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return alltype(context)

    def get_queryset(self):
        return Product.objects.filter(category_model__slug=self.kwargs['category_model_slug'])

class MainPageType(ListView):
    model = Product
    template_name = 'OnlineShop/shop.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return alltype(context)

    def get_queryset(self):
        return Product.objects.filter(category_for__slug=self.kwargs['category_for_slug'])

class AboutPage(ListView):
    model = Product
    template_name = 'OnlineShop/about.html'

class HomePage(ListView):
    model = Product
    template_name = 'OnlineShop/index.html'


class HomePage(ListView):
    model = Product
    template_name = 'OnlineShop/index.html'

class ProductDetailView(FormView, DetailView):
    model = Product
    template_name = 'OnlineShop/shop-single.html'
    slug_url_kwarg = 'product_slug'
    form_class = CartAddProductForm
    success_url = reverse_lazy('cart_detail')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['items'] = Product.objects.filter(category_model = kwargs['object'].category_model)
        context['cart_product_form'] = self.get_form()
        return context



def login_page(request):
    if request.user is not None:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'OnlineShop/login.html')

        context = {}
        return render(request, 'OnlineShop/login.html', context)
    else:
        return redirect('index')


def register(request):
    if request.user is not None:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form': form}
        return render(request, 'OnlineShop/registration.html', context)
    else:
        return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('login')


