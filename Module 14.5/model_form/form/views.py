from django.shortcuts import render, redirect
from . import models

# Create your views here.
def forms(request):
    MyModel = models.MyModel.objects.all()
    return render(request, 'form.html', {'data' : MyModel})

def delete_model(request, roll):
    std = models.MyModel.objects.get(pk = roll).delete()
    return redirect("form")
