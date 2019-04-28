from django.shortcuts import render

# Create your views here.
def about(request):
    title = "Sobre Nosotros"
    context = {
        "title": title
       
    }    
    return render(request, "about.html", context)