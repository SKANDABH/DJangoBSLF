from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Category
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('my_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})


@login_required
def my_blog_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_blog_posts.html', {'posts': posts})


def blog_posts(request):
    categories = Category.objects.all()
    return render(request, 'blog/blog_posts.html', {'categories': categories})
    # blog_posts = BlogPost.objects.filter(is_draft=False)

    # # Group blog posts by category
    # categories = Category.objects.all()
    # grouped_posts = {category: blog_posts.filter(category=category) for category in categories}

    # context = {
    #     'grouped_posts': grouped_posts,
    # }
    # return render(request, 'blog/patient_blog_posts.html', context)


# blog/views.py


def blog_posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = BlogPost.objects.filter(category=category, is_draft=False)
    print(f"Category: {category.name}, Number of Posts: {posts.count()}")
    return render(request, 'blog/blog_posts_by_category.html', {'posts': posts, 'category': category})


def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
