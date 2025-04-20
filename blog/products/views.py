from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product
from blog.models import Category, Post  # Added Post model import


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def product_list(request):
    categories = Category.objects.all()
    category_slug = request.GET.get('category')
    sort = request.GET.get('sort', 'name')
    
    products = Product.objects.all()
    if category_slug:
        products = products.filter(categories__slug=category_slug)
    
    # Handle sorting
    if sort == 'name':
        products = products.order_by('name')
    elif sort == '-name':
        products = products.order_by('-name')
    elif sort == 'price':
        products = products.order_by('price')
    elif sort == '-rating':
        products = products.order_by('-rating')[:3]
    
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'category_slug': category_slug,
    })


def home(request):
    posts = Post.objects.order_by('-date_posted')[:6]  # Fixed: changed 'posts' to 'Post'
    products = Product.objects.filter(featured=True)[:3]
    return render(request, 'blog/home.html', {'posts': posts, 'products': products})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fixed: changed 'post' to 'Post'
    return render(request, 'blog/post_detail.html', {'post': post})


def category_list(request):
    categories = Category.objects.all()  # Fixed: changed 'category' to 'Category'
    return render(request, 'blog/category_list.html', {'categories': categories})