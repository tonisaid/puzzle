from django.shortcuts import render
from .models import UserInputs
from .forms import UserInputForm

# Create your views here.
context = {
        'form': UserInputForm(),
        'info': UserInputs.objects.all().last(),
    }
def index(request):
    
    
    if request.method == 'POST':
        add_info = UserInputForm(request.POST)
        if add_info.is_valid():
            add_info.save()

    return render(request, 'index.html', context)