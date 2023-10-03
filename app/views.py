from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.forms import PersonForm
from app.models import Person

# Create your views here.

# Create Read


def index(request):
    if request.method == "GET":
        return render(request, 'index.html', {
            'title': 'Index page', 'form': PersonForm()})
    else:
        f = PersonForm(request.POST)
        if f.is_valid():
            p = Person.objects.create(**f.cleaned_data)
            p.save()
        return HttpResponseRedirect('/')

# Update


def update(request, pk):
    if request.method == "GET":
        pf = Person()
        data = pf.objects.all.get(id=pk)
        return render(request, 'update.html', {'title': 'Update page', 'form': PersonForm(data)})
