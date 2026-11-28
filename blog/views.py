from django.shortcuts import render

# Cremos una primera view creado una función (def) llamada post_list que acepta request y return una función render que reproduce (construye)
from django.utils import timezone #añadimos esta línea para que viues pueda puesués filtrar u ordenar por fechas de publicación
# nuestra plantilla blog/post_list.html.your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

