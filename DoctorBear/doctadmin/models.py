from django.db import models

# Create your models here.

class UserType(models.Model):
	"""docstring for UserType:0用户未选择身份/1普通用户/2医师/3管理员"""
	# def __init__(self, arg):
	# 	super(UserType, self).__init__()
	# 	self.arg = arg
	UserTypeID = models.AutoField(primary_key=True)
	UserTypeName = models.CharField(max_length=20)
	def __str__(self):
		return self.UserTypeName
# (用户分类表)UserType:
# UserTypeID:int 11(autoincrement, primary key)
# UserTypeName:varchar (1普通用户/2医师/3管理员)
# UserTypeID==0用户未选择身份

class User(models.Model):
	"""docstring for User:user info"""
	# def __init__(self, arg):
	# 	super(User, self).__init__()
	# 	self.arg = arg
	UserID = models.CharField(max_length=20)
	UserName = models.CharField(max_length=20)
	UserIcon = models.CharField(max_length=100)
	# UserTypeID = models.ForeignKey(UserType,on_delete=models.CASCADE)
	UserTypeID = models.IntegerField(default=0)
	UserDetail = models.CharField(max_length=200)	

# 用户
# (用户个人信息表)User:
# UserID:varchar 50
# UserName:varchar 20
# UserIcon:varchar  100
# UserTypeID:
# UserDetail:varchar 200

