from django.shortcuts import render

# Create your views here.
def about(request):
    title = "About"
    context = {
        "title": title
       
    }    
    return render(request, "about.html", context)