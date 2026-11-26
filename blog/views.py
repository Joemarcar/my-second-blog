from django.shortcuts import render

# Cremos una primera view creado una función (def) llamada post_list que acepta request y return una función render que reproduce (construye)
# nuestra plantilla blog/post_list.html.your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})