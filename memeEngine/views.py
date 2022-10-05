from multiprocessing import context
from django.shortcuts import render
from .models import Meme
from django.views.generic import  ListView, DetailView, CreateView
from .forms import uploadForm


#def test(request):
    #context={}
    #return render (request, 'test.html', context)


class homeView (ListView):
    model = Meme
    template_name = 'home.html'

class detailView (DetailView):
    model = Meme
    template_name = 'detail.html'

class uploadView (CreateView):
    model = Meme
    template_name = 'upload.html'
    form_class = uploadForm

def searchResult (request):
    if request.method == "POST":
        search = request.POST['search']
        memes= Meme.objects.filter(tag__name__icontains=search)

        return render(request, 'search.html', {'search':search, 'memes':memes})

    else:
                return render(request, 'search.html')