from django.shortcuts import render
from library.models import MusicItem
from .forms import MusicItemForm
from django.contrib import messages

# Create your views here.
def library(request):
    items = MusicItem.objects.all()
    context = {
        'items': items
    }
    return render(request, 'library_index.html', context)


def library_add(request):
    form = MusicItemForm()
    if request.method == 'POST':
        form = MusicItemForm(request.POST)
        if form.is_valid():
            item = MusicItem(
                inventory_num=form.cleaned_data['inventory_num'],
                title=form.cleaned_data["title"],
                composer_last=form.cleaned_data["composer_last"],
                composer_first=form.cleaned_data["composer_first"],
                arranger_last=form.cleaned_data["composer_last"],
                arranger_first=form.cleaned_data["composer_first"],
                ensemble=form.cleaned_data["ensemble"],
                style=form.cleaned_data["style"],
                difficulty=form.cleaned_data["difficulty"],
                rating=form.cleaned_data["rating"],
                last_performed=form.cleaned_data["last_performed"],
                organized=form.cleaned_data["organized"],
                notes=form.cleaned_data["notes"],
            )
            item.save()

            items = MusicItem.objects.all()

            context = {
                'items': items,
                'add_flag': True,
            }

            return render(request, 'library_index.html', context)

    context = {
        "form": form,
    }

    return render(request, 'library_add.html', context)


def library_detail(request, pk):
    item = MusicItem.objects.get(pk=pk)

    if request.method == 'POST':
        item.delete()

        items = MusicItem.objects.all()
        context = {
            'items': items,
            'del_flag': True,
        }
        return render(request, 'library_index.html', context)

    context = {
        'item': item,
    }

    return render(request, 'library_detail.html', context)
