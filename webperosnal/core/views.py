from django.shortcuts import render, HttpResponse

html_base="""
    "<h1> Mi web Personal</h1>
     <u1>
         <li><a href="/">Portada</a></li>
         <li><a href="/about/">Acerca de...</a></li>
         <li><a href="/portfolio/">Portafolio</a></li>
         <li><a href="/contact/">Contacto del grupo</a></li>
    </u1>
"""
# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def Contact(request):
    return render(request, "core/contact.html")
