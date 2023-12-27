from django.shortcuts import render

def index(request):
    return render(request, 'templates/index.html')

def about(request):
    return render(request, 'templates/about.html')

def contact(request):
    return render(request, 'templates/contact.html')

def project_link_view(request):
    return render(request, "templates/project_links.html")