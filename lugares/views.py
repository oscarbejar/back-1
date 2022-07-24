from django.shortcuts import render
from lugares.models import Lugares

# Create your views here.
def lugares(request):

    lugares=Lugares.objects.all()

    return render(request, 'lugares/lugares.html',{"lugares": lugares})