# from django.shortcuts import render
from django.http import HttpResponse
from doctadmin.models import *
# from django.template import RequestContext 
from django.shortcuts import render, render_to_response
from django import forms
from django.utils.six import BytesIO
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from .serializers import UserSerializer, GroupSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from doctadmin.models import User
from doctuser.serializers import UserSerializer

def index2(request):
	alllist = UserType.objects.all()
	return HttpResponse(alllist[0].UserTypeName)
# Create your views here.
def login(request,xxid):
	return HttpResponse(xxid)
	# return [b'xx']
	# return render_to_response('index.html',context_instance=RequestContext(request))

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
def handle(request):
	if request.method == "POST":
		
		print("----"+request.POST['UserID'])
		data = JSONParser().parse(request)
		# serializer = UserSerializer(data=data)
		# if serializer.is_valid():
		# 	return JSONResponse(serializer.data, status=201)
		# return JSONResponse(serializer.errors, status=400)
		return HttpResponse(request.POST['UserID'])

		
# def mypost(request):
# 	if request.method == "POST":
# 		# myform = Myform(request.POST, request.FILES)
# 		myform = forms.Form(request.POST, request.FILES)
# 		# return HttpResponse(request.POST['UserIcon'])
# 		if myform.is_valid():
# 	# 		user = User()
# 	# 		user.UserID = myform.cleaned_data['UserID']
# 	# 		user.UserName = myform.cleaned_data['UserName']
# 		# user.UserIcon = myform.cleaned_data['UserIcon']
# 	# 		user.UserTypeID = myform.cleaned_data['UserTypeID']
# 	# 		user.UserDetail = myform.cleaned_data['UserDetail']
# 	# 		user.save()
# 			return HttpResponse(str(len(request.POST))+":"+str(len(request.FILES)))
# 		else:
# 			return HttpResponse(myform.errors.as_json(escape_html=False))

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

