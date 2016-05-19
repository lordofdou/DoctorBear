# from django.shortcuts import render
from django.http import HttpResponse
from .models import UserType
def index(request):
	alllist = UserType.objects.all()
	print("==="+alllist)
	return HttpResponse(alllist)
# Create your views here.
