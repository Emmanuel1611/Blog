from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from products.models import Product
from .forms import ContactForm  
from django.core.mail import send_mail
from .forms import NewsletterForm

def home(request):
    posts = Post.objects.order_by('-date_posted')[:5]
    products = Product.objects.all()[:3]
    return render(request, 'blog/home.html', {'posts': posts, 'products': products})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

from django.db.models import Q
def search(request):
    query = request.GET.get('q')
    posts = products = None
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'blog/search.html', {'posts': posts, 'products': products, 'query': query})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form (e.g., send email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['muhindoemma39@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'blog/contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # Save email to database or integrate with Mailchimp later
            email = form.cleaned_data['email']
            # Example: Save to a model (create NewsletterSubscriber model if needed)
            return render(request, 'blog/newsletter.html', {'form': form, 'success': True})
    else:
        form = NewsletterForm()
    return render(request, 'blog/newsletter.html', {'form': form})