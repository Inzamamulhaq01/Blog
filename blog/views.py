from django.shortcuts import render

def page_not(request,exception):
    return render(request,'404.html',status=404)