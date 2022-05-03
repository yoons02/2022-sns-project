from django.shortcuts import render

# Create your views here.

# mainpage
def showmain(request):
    return render(request, 'main/show.html')

# contactpage
def showcontact(request):
    return render(request, 'main/contact.html')