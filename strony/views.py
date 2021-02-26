from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
    return render(request,"contacts.html",{})


def about_view(request,*args,**kwargs):
    
    my_dictionary={
        "my_pos1":"tekst z pozycji pierwszej",
        "my_pos2":"tekst z pozycji drugiej",
        "my_pos3":"tekst z pozycji trzeciej",
        "my_pos1_int":23,
    }
    return render(request,"about.html",my_dictionary)