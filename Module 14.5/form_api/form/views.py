from django.shortcuts import render
from . forms import ExampleForm
# Create your views here.
def forms(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')        
        return render(request, 'forms.html', {'name' : name, 'email': email})
    
    return render(request, 'forms.html')

def djangoForm(request):
    form = ExampleForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'djangoForms.html', {'form' : form})