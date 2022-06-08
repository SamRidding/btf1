from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm, AddPostForm, EditPostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-posted_on")
    template_name = "home.html"


class BlogPost(View):

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

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            comment_form = CommentForm()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/blog_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": comment_form,
            },
        ) 


def AddPost(request):

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
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


def EditPost(request, slug):

    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            
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


def DeletePost(request, slug):

    if request.user.is_staff:
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('home')
