from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post


@login_required
def saved_releases(request):
    """Displays releases saved by the user in their user profile"""

    new = Post.objects.filter(save_release=request.user)
    return render(request,
                  'userprofile/userprofile.html',
                  {'new': new})


@login_required
def add_release(request, id):
    """
    Allows user to add or remove releases they have saved to their
    user profile
    """

    post = get_object_or_404(Post, id=id)
    if post.save_release.filter(id=request.user.id).exists():
        post.save_release.remove(request.user)
        messages.success(request, 'The release has been removed from your \
                                   list.')
    else:
        post.save_release.add(request.user)
        messages.success(request, 'The release has been added to your list.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
