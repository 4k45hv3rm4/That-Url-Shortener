from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from .models import ShortURL
from .forms import SubmitURLForm
from analytics.models import ClickEvent


class HomeView(View):

    def get(self, request, *args, **kwargs):
        the_form = SubmitURLForm()

        context = {
        "title":"Submit URL",
        "form": the_form
        }
        return render(request, 'app/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        context = {
        "title":"Submit URL",
        "form": form
        }
        print(form)
        template = 'app/home.html'

        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = ShortURL.objects.get_or_create(url=new_url)
            context = {
            "obj" : obj,
            "created" : created
            }
            if created :
                 template = "app/success.html"
            else:
                template = "app/already-exists.html"

        return render(request, template, context)


class UrlRedirectView(View):

    def get(self, request, *args, **kwargs):
        shortcode = kwargs.get('shortcode')
        qs = ShortURL.objects.filter(shortcode__iexact = shortcode)
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
