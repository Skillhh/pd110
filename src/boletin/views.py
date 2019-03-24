from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
    title = "Formulario"
    if request.user.is_authenticated:
        title = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance)
        print(instance.timestamp)
    # form = RegForm(request.POST or None)
    # if form.is_valid():
    #     form_data = form.cleaned_data
    #     abc = form_data.get("email")
    #     abc2 = form_data.get("nombre")
    #     obj = Registrado.objects.create(email=abc, nombre=abc2)

    context = {
        "title": title,
        "el_form": form,
    }
    return render(request, "inicio.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print( key, " ", form.cleaned_data.get(key))
        from_nombre = form.cleaned_data.get("nombre")
        from_email = form.cleaned_data.get("email")
        from_mensaje = form.cleaned_data.get("mensaje")
        # print( nombre, email, mensaje )
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from] 
        email_mensaje = ("%s: %s enviado por %s" %(from_nombre, from_mensaje, from_email ))
        send_mail(
            email_from,
            [email_to],
            asunto,
            email_mensaje,            
            fail_silently=False
            )
    context = {
        "form" : form,
    }

    return render(request, "forms.html", context)
