from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import DetailView
from django.core.paginator import Paginator



def Post_today(request):

    if 'q' in request.GET:
        q = request.GET['q']
        articles = Post.objects.filter(Q(title__icontains=q) | Q(book__icontains=q))
    else:
        articles = Post.objects.all().order_by('-id')
        q = None

    # def get_client_ip(request):
    #     address = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if address:
    #         ip = address.split(',')[-1].strip()
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    #     return ip
    #
    # ip = get_client_ip(request)
    # user = IpModel(user=ip)
    # print(ip)
    #     # results = IpModel.objects.filter(Q(user__icontains=ip))
    #     # if len(results) == 1:
    #     #     print("already exists ")
    #     #
    #     # elif len(results) > 1:
    #     #     print("already exists ")
    #     #
    #     # else:
    #     #     user.save()
    #     #
    #     # con = IpModel.objects.all().count()
    #     # print("user is ...", con)
    #     #


    return render(request, 'post.html', {"articles": articles, "q": q})

class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = 'post'



def user_page(request):
    if request.method == "POST":
        model = User()
        model.name = request.POST.get("name")
        model.username = request.POST.get("username")
        model.phone_number = request.POST.get("phone_number")
        model.message = request.POST.get("message")

        model.save()
        return render(request, "index.html")

    else:
        return render(request, "index.html")




