from django.shortcuts import redirect, render, redirect
from .forms import FormularioContacto

from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
     formularioc=FormularioContacto()

     if request.method=="POST":
          formularioc=FormularioContacto(data=request.POST)
          if formularioc.is_valid():
               nombre=request.POST.get("nombre")
               mail=request.POST.get("mail")
               contenido=request.POST.get("contenido")

               mail=EmailMessage("mensaje desde app Infotravel",
               "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre,mail,contenido),
               "",["infotravelifts16@yahoo.com"],reply_to=[mail])

               try:
                    mail.send()
                    return redirect("/contacto/?valido")
               except:
                    return redirect("/contacto/?novalido")

     return render(request, 'contacto/contacto.html',{'miformulario':formularioc})