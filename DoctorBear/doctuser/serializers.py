# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from doctadmin.models import User


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
# class UserSerializer(serializers.Serializer):
# 	"""docstring for UserSerializer"""
# 	# def __init__(self, arg):
# 	# 	super(UserSerializer, self).__init__()
# 	# 	self.arg = arg
# 	pk = models.IntegerField()
# 	UserID = models.CharField(max_length=20)
# 	UserName = models.CharField(max_length=20)
# 	UserIcon = models.FileField()
# 	UserTypeID = models.IntegerField(default=0)
# 	UserDetail = models.CharField(max_length=200)	
class UserSerializer(serializers.ModelSerializer):
	"""docstring for UserSerializer"""
	# def __init__(self, arg):
	# 	super(UserSerializer, self).__init__()
	# 	self.arg = arg
	class Meta:
		model = User
		fields = ('UserID','UserName','UserIcon','UserTypeID','UserDetail')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')