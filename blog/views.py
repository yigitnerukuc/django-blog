from django.shortcuts import render
from django.utils import timezone
from .models import Yazi
# Create your views here.

def post_list(request):
    yazilar = Yazi.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
    return render(request, 'blog/post_list.html', {'yazilar': yazilar})
