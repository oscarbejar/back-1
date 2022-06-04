from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


class VRegistro(View):
    
    def get(self,request): #el get nos muestra el formulario

        form=UserCreationForm() #variable que almacena el formulario a ver
        return render(request, "registro/registro.html",{"form":form})
    
    def post(self,request):    #gestiona el envio de info del formulario
        form=UserCreationForm(request.POST)   #almacena el form con la info que el user haya introducido
        
        if form.is_valid():
        
            usuario=form.save()      #guarda la info del formulario; esta info va a la db a traves de la instruccion ".save"
       
            login(request, usuario) #una vez realizado el registro hace un login automatico y redirecciona al home

            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"registro/registro.html",{"form":form})