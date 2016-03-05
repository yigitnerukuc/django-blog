from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Yazi
# Create your views here.

def post_list(request):
    yazilar = Yazi.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
    return render(request, 'blog/post_list.html', {'yazilar': yazilar})

def post_detail(request,pk):
    yazi = get_object_or_404(Yazi, pk=pk)
    return render(request, 'blog/post_detail.html', {'yazi': yazi})
