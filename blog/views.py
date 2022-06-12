import random
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, AddPostForm, EditPostForm


def home_page(request):
    """View to display posts and featured posts on home page"""

    posts = Post.objects.filter(status=1).order_by("-posted_on")[:6]
    featuredpost = random.choice(posts)

    template = "home.html"
    context = {
        "posts": posts,
        "featuredpost": featuredpost,
    }

    return render(request,
                  template,
                  context)


class Blog(generic.ListView):
    """View to display posts on blog page"""

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-posted_on")
    template_name = "blog/blog.html"


def search_blog(request):
    """View to search blog posts"""

    if request.method == "POST":
        searched = request.POST.get('searched')
        results = Post.objects.filter(title__icontains=searched)
        return render(request, 'blog/search_blog.html',
                      {'searched': searched,
                       'results': results, })
    else:
        return render(request, 'blog/search_blog.html')


class BlogPost(View):
    """
    View for individual blog posts, returning all post model
    data & allowing users to view and post comments on each post
    """

    def get(self, request, slug, *args, **kwargs):
      
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-posted_on")
        saved = bool

        if post.save_release.filter(id=request.user.id).exists():
            saved = True

        return render(
            request,
            "blog/blog_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
                "saved": saved,
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-posted_on")

        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                comment_form = CommentForm()
                messages.success(request, 'Your comment has been posted')
            else:
                comment_form = CommentForm()
        else:
            messages.error(request, 'You need to be logged in to post \
                           comments')
            return redirect(reverse('blog_post', args=[post.slug]))

        return render(
            request,
            "blog/blog_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": comment_form,
            },
        )


@login_required
def delete_comment(request, comment_id):
    """Allow admins or users to delete comments"""

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        messages.success(request, 'The comment has been deleted')
        return redirect(reverse('blog_post', args=[comment.post.slug]))


@login_required
def add_post(request):
    """Allow admins to create new posts from the front end of the site"""

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, "The post has been added to the blog.")
            return redirect(reverse('blog_post', args=[post.slug]))
        else:
            messages.error(request,
                           "The post could not be submitted. \
                            Please try again.")
            return redirect('add_post')
    else:
        form = AddPostForm()

    template = "blog/add_post.html"

    context = {
        "form": form,
    }

    return render(request,
                  template,
                  context)


@login_required
def edit_post(request, slug):
    """Allow admins to edit posts from the front end of the site"""

    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated')
            return redirect(reverse('blog_post', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update - please try again')
    else:
        form = EditPostForm(instance=post)

    template = "blog/edit_post.html"

    context = {
        "form": form,
        "post": post,
        "edit_post": True,
    }

    return render(request,
                  template,
                  context)


@login_required
def delete_post(request, slug):
    """Allow admins to delete posts form front end of the site"""

    if request.user.is_staff:
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        messages.success(request, "The post has been deleted")
        return redirect('home')
    else:
        messages.error(request,
                       'You do not have permission to delete this post.')
        return redirect(reverse('blog_post', args=[post.slug]))
