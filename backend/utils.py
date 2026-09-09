from django.shortcuts import get_object_or_404, redirect
from app.models import URL


def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.visit_count +=1 
    url.save(update_fields=['visit_count'])
    return redirect(url.original_url)