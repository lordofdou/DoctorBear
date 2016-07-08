# from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def index(request):
	alllist = UserType.objects.all()

	return HttpResponse(alllist[1].UserTypeName)
# Create your views here.
