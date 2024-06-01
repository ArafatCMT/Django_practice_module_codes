from django.shortcuts import render
from first_app.forms import AdmissionForm, HealthModelForm
# Create your views here.
def admission_form(request):
    form = AdmissionForm()
    return render (request, 'admission_form.html', {'form': form})

def health_form(request):
    if request.method == 'POST':
        form = HealthModelForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = HealthModelForm()
    return render (request, 'health_form.html', {'form': form})



