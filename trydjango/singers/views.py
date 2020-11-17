from django.shortcuts import render, redirect

from .forms import SingerForm

from .models import Singer

# Create your views here.


def singer_create_view(request):
    form = SingerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SingerForm()
    context = {
        'form': form
    }
    return render(request, "singers/singer_create.html", context)


def singer_list_view(request):
    queryset = Singer.objects.all().order_by('-date')
    context = {
        "object_list": queryset
    }
    return render(request, "singers/singer_list.html", context)


def singer_delete_view(request, id):
    obj = Singer.objects.filter(id=id)
    obj.delete()
    return redirect('/singers/')