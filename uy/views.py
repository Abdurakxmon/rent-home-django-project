from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.views.generic import ListView
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.number = request.POST.get('number')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request, 'Thank you we will ask you.')
        return redirect('uy:home')
    return render(request, 'index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('uy:home')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                phone = request.POST.get('phone')
                Profile.objects.create(
                user=user,
                name=user.username,
                phone=phone,
                )
                messages.success(request, 'Success! '+username+' registered. Please log in.')
                return redirect('uy:login')
        context = {'form':form}
        return render(request, "accounts/royhat.html", context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('uy:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('uy:home')
            else:
                messages.info(request, 'Passwor or Username wrong!')
        context={}
    return render(request, "accounts/kirish.html", context)
def logout_s(request):
    return render(request, "accounts/logout.html")

@login_required(login_url='uy:login')
def logout_view(request):
    logout(request)
    return redirect('uy:home')

def ijaraga_uy(request):
    qw = New_home.objects.all().order_by('-id')
    all_home = Paginator(qw,5)
    page = request.GET.get('page')
    try:
        home = all_home.page(page)
    except PageNotAnInteger:
        home = all_home.page(1)
    except EmptyPage:
        home = all_home.page(all_home.num_pages)
    context = {
        'home':home,
    }
    return render(request, 'olish.html',context)
@login_required(login_url='uy:login')
def ijaraga_uy_qoyish(request):
    if request.method == "POST":
        home = New_home()
        prof=Profile.objects.get(user=request.user)
        home.user=prof
        home.region = request.POST.get('region')
        home.district = request.POST.get('district')
        home.cost = request.POST.get('cost')
        home.number_of_rooms = request.POST.get('number_of_rooms')
        home.desc = request.POST.get('desc')
        home.img_1 = request.FILES['image_1']
        home.img_2 = request.FILES['image_2']
        home.img_3 = request.FILES['image_3']
        home.save()
        return redirect('/')
    return render(request, 'qoyish.html')


class PostViewDetail(View):
    def get(self,request,id):
        home = get_object_or_404(New_home, id=id)
        context = {'home':home,}
        return render(request, 'Home.html', context)

class FilterPostsView(ListView):
    model = New_home
    template_name = 'list.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        query1 = self.request.GET.get('p')
        object_list = New_home.objects.filter(
            Q(region__contains = query,district__contains = query1)
            )
        return object_list
