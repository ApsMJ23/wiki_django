from django.shortcuts import render
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
import markdown2
from django.utils.html import format_html

#Creating a django Form
class add_entry_form(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}),help_text="Write your content in Markdown. (Please refer to 'markdownguide.org')")

# Create your views here.

def index(request):
    en = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries" : en,
    })

#THIS SHOWS ENTRY
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


#THIS ADDS ENTRY
def add_entry(request):
    if request.method == "POST":
        new_entry = add_entry_form(request.POST)
        if new_entry.is_valid():
            new_title = request.POST['title']
            new_content = request.POST['content']
            util.save_entry(new_title,new_content)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'encyclopedia/error.html',{
                "form" : new_entry
            })
    return render(request, "encyclopedia/add.html",{
        "form":add_entry_form()
    })   


#SEARCH BAR
def search_entry(request):
    title = request.GET.get("q")
    entry1 = util.list_entries()
    for i in entry1:
        if i.lower() == title.lower(): 
            show_entry = format_html(markdown2.markdown(util.get_entry(i)))
            return render(request, "encyclopedia/entry.html", {
                "entry" : show_entry,
                "title" : title  
            })
    if not title:
        return render(request, "encyclopedia/error.html")
    
    