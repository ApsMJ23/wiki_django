from django.shortcuts import render
from . import util
import markdown2
from django.utils.html import format_html

# Create your views here.

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries" : util.list_entries()
    })


def show_entry(request, title):
    entry1 = util.list_entries()
    for i in entry1:
        if title == i:
            try:
                show_entry = format_html(markdown2.markdown(util.get_entry(title)))
            except:
                show_entry = ""
            
            
    context = {
        "title": title,
        "entries": entry1
    }
    if not title in entry1:
        return render(request, "encyclopedia/error.html", context)
    
    return render(request, "encyclopedia/entry.html", {
       "entry" : show_entry,
       "title" : title  
    })

