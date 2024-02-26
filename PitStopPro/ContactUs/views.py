from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact') 
    else:
        form = ContactForm()

    context = {'form' : form}
    return render(request, 'contact.html', context)