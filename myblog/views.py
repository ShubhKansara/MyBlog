from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic


def homepage(request):
    # return HttpResponse('Homepage')
    return render(request, 'myblog/index.html')
def about(request):
    # return HttpResponse("ABOUT")
    return render(request, 'myblog/about.html')

# class HomepageView(generic.ListView):
#     template_name = 'myblog/index.html'

# class AboutView(generic.ListView):
#     template_name = 'myblog/about.html'