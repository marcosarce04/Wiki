from django.shortcuts import render
import markdown2
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
from random import randint


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    desc = util.get_entry(entry)
    if not desc:
        desc = f'Entry for "{entry}" was not found.'
    return render(request,"encyclopedia/entry.html", {
        "entry": markdown2.markdown(desc),
        "title": entry
    })

def search(request):
    q = request.GET.get('q')
    desc = util.get_entry(q)
    entries = util.list_entries()
    if not desc:
        return render(request, "encyclopedia/index.html", {
        "entries": list(filter(lambda entry: q.lower() in entry.lower(), entries))
    })

    return render(request,"encyclopedia/entry.html", {
        "entry": markdown2.markdown(desc),
        "title": q
    })

def newpage(request):
    return render(request, "encyclopedia/newpage.html")

def savenewpage(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    if not title or not content:
        return render(request, "encyclopedia/error.html", {
        "message": "Title or content missing"
    })
    else:
        if util.get_entry(title):
            return render(request, "encyclopedia/error.html", {
        "message": "This entry already exist."
    })
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=(title,)))

def edit(request):
    title = request.GET.get('q')
    return render(request, "encyclopedia/editpage.html", {
        "content": util.get_entry(title),
        "title": title
    })

def savedition(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    if not content:
        return render(request, "encyclopedia/error.html", {
        "message": "Content can't be empty."
    })
    else:
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry", args=(title,)))

def random(request):
    list = util.list_entries()
    return HttpResponseRedirect(reverse("entry",args=(list[randint(0,len(list)-1)],)))
