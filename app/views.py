from django.shortcuts import render, redirect
from django.views.generic import FormView

from app.forms import EmployerModelForm
from app.models import Employer


def thanks_page(request):
    return render(request, 'app/thanks.html')


def form_page(request):
    employer = Employer.objects.all()
    context = {
        'employers': employer
    }

    if request.method == 'POST':
        form = EmployerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        context['form'] = form
    return render(request, 'app/index.html', context)
