from django.http import HttpResponseRedirect
from django.conf import settings

DEFAULT_REDIRECT_URL = getattr(settings, 'DEFAULT_REDIRECT_URL', ' http://www.4kash.com:8000')

def wildcart_redirect(request, path=None):
    new_url = DEFAULT_REDIRECT_URL
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL+'/'+path
    return HttpResponseRedirect(new_url)
