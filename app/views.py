from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from app.forms import PersonForm
from app.models import Person

# Create your views here.


def create(request):
    '''Create'''
    if request.method == "GET":
        return render(request, 'create.html', context={'title': 'Create page', 'form': PersonForm()})
    else:
        pf = PersonForm(request.POST)
        if pf.is_valid():
            Person.objects.create(**pf.cleaned_data)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("bad data")


def index(request):
    '''Read'''
    persons = Person.objects.all()
    return render(request, 'index.html', context={
        'title': 'Index page', 'persons': persons})


def update(request, pk):
    if request.method == "GET":
        try:
            person = Person.objects.get(id=pk)
        except Exception as e:
            print(f"Exception {e} was risen while trying update a record")
            return HttpResponseNotFound('Person not found')
        return render(request, 'update.html', {'title': 'Update page', 'person': person, 'form': PersonForm()})
    else:
        pf = PersonForm(request.POST)
        if pf.is_valid():
            Person.objects.update(**pf.cleaned_data)
            return HttpResponseRedirect('/')


def delete(request, pk):
    try:
        Person.objects.get(id=pk).delete()
        return HttpResponseRedirect('/')
    except Exception as e:
        print(f"Exception {e} was risen when trying delete record")
        return HttpResponseNotFound('Person not found')
