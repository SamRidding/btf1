from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Mix


class MixPage(View):
    """View for individual mixes, returning all mix model data"""

    def get(self, request, slug, *args, **kwargs):

        queryset = Mix.objects.all()
        mix = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "mixes/mix_page.html",
            {
                "mix": mix,
            }
        )


class Mixes(generic.ListView):
    """View to display all mixes"""

    model = Mix
    queryset = Mix.objects.all().order_by("-posted_on")
    template_name = "mixes/all.html"
