from django.shortcuts import render, redirect, get_object_or_404

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
    if obj is not None:
        return redirect('/singers/')


def singer_update_view(request, id=id):
    obj = get_object_or_404(Singer, id=id)
    form = SingerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "singers/singer_update.html", context)