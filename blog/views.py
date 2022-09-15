from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import PostForm
from .models import PostModel
from sympy import *


def get_secured_data(p):
	if len(p)%2==1:
		p=p+' '
	K = Matrix(([2, 1], [5, 3]))
	Km = Matrix(([1, 2], [3, 7]))

	c = ''
	cm = ''
	i = 0
	while i < len(p):
		P = Matrix((ord(p[i])-32, ord(p[i + 1])-32))
		C = K * P
		c = c + chr((C[0] % 97)+32) + chr((C[1] % 97)+32)
		i = i + 2
	i = 0
	while i < len(c):
		P = Matrix((ord(c[i]), ord(c[i + 1])))
		C = Km * P
		cm = cm + chr((C[0] % 97)+32) + chr((C[1] % 97)+32)
		i = i + 2
	return cm


def index(request):
	posts = PostModel.objects.all()

	context = {
		'page_title':'Data anda akan tersimpan dengan aman',
		'posts':posts,
	}

	return render(request,'blog/index.html',context)

def create(request):
	post_form = PostForm()

	if request.method == 'POST':
		PostModel.objects.create(
				judul 		= get_secured_data(request.POST.get('nama')),
				body		= get_secured_data(request.POST.get('alamat')),
				category	= get_secured_data(request.POST.get('nik')),
			)

		return HttpResponseRedirect("/blog/")


	context = {
		'page_title':'Pendaftaran',
		'post_form':post_form
	}

	return render(request,'blog/create.html',context)














