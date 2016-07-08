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

class User(models.Model):
	"""docstring for User:user info"""
	# def __init__(self, arg):
	# 	super(User, self).__init__()
	# 	self.arg = arg
	UserID = models.CharField(max_length=20)
	UserName = models.CharField(max_length=20)
	UserIcon = models.FileField(upload_to = './media/upload/icon')
	UserTypeID = models.IntegerField(default=0)
	UserDetail = models.CharField(max_length=200)	

class PathemaType(models.Model):
	"""docstring for PathemaType"""
	# def __init__(self, arg):
	# 	super(PathemaType, self).__init__()
	# 	self.arg = arg
	PathemaTypeID = models.AutoField(primary_key=True)
	PathemaTypeName = models.CharField(max_length=50)
	PathemaTypeDetail = models.IntegerField(default=1)
	SuperType = models.IntegerField(default=0)


class Pathema(models.Model):
	"""docstring for Pathema"""
	# def __init__(self, arg):
	# 	super(Pathema, self).__init__()
	# 	self.arg = arg
	PathemaID =	models.AutoField(primary_key=True)	
	PathemaName = models.CharField(max_length=50)
	PathemaTypeID = models.IntegerField(default=0)
	PathemaCont = models.TextField() 					



class Medicine(models.Model):
	"""docstring for Medicine"""
	# def __init__(self, arg):
	# 	super(Medicine, self).__init__()
	# 	self.arg = arg
	MedicineID = models.AutoField(primary_key=True)	
	MedicineName = models.CharField(max_length=50)
	MedicineCont = models.TextField()


class Hospital(models.Model):
	"""docstring for Hospital"""
	# def __init__(self, arg):
	# 	super(Hospital, self).__init__()
	# 	self.arg = arg
	HospitalID = models.AutoField(primary_key=True)	
	HospitalName = models.CharField(max_length=50)
	HospitalCont = models.TextField()
		
class Article(models.Model):
	"""docstring for Article"""
	# def __init__(self, arg):
	# 	super(Article, self).__init__()
	# 	self.arg = arg
	ArticleID = models.AutoField(primary_key=True)
	ArticleTitile = models.CharField(max_length=30)
	ArticleDesc = models.TextField()
	ArticlePic = models.FileField(upload_to = './media/upload/article')
	PathemaTypeID = models.IntegerField(default=0)
	UserID = models.IntegerField(default=0)
	CreateTime = models.DateField(auto_now_add=True)
	Like = models.IntegerField(default=0)
	Comm = models.IntegerField(default=0)
	Send = models.IntegerField(default=0)
		

class Community(models.Model):
	"""docstring for Community"""
	# def __init__(self, arg):
	# 	super(Community, self).__init__()
	# 	self.arg = arg
	CommunityID = models.AutoField(primary_key=True)
	CommunityTitle = models.CharField(max_length=30)
	CommunityDesc = models.TextField()
	CommunityPic = models.FileField(upload_to = './media/upload/community')
	PathemaTypeID = models.IntegerField(default=0)
	UserID = models.IntegerField(default=0)
	CreateTime = models.DateField(auto_now_add=True)
	Like = models.IntegerField(default=0)
	Comm = models.IntegerField(default=0)
	Send = models.IntegerField(default=0)

class Favourite(models.Model):
	"""docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
	FavouriteID = models.AutoField(primary_key=True)
	UserID = models.IntegerField(default=0)
	ArticleID = models.IntegerField(default=0)
	CommunityID = models.IntegerField(default=0)			


class Comment(models.Model):
	"""docstring for Comment:(0未读／1已读)"""
	# def __init__(self, arg):
	# 	super(Comment, self).__init__()
	# 	self.arg = arg
	CommentID = models.AutoField(primary_key=True)
	ArticleID = models.IntegerField(default=0)
	CommunityID = models.IntegerField(default=0)
	UserID = models.IntegerField(default=0)
	Content = models.CharField(max_length=255)
	CreateTime = models.DateField(auto_now_add=True)
	Read = models.IntegerField(default=0)	

class Subscribe(models.Model):
	"""docstring for Subscribe:(0未订阅／1已订阅)"""
	# def __init__(self, arg):
	# 	super(Subscribe, self).__init__()
	# 	self.arg = arg
	SubscribeID = models.AutoField(primary_key=True)
	UserID = models.IntegerField(default=0)
	PathemaTypeID = models.IntegerField(default=0)
	sub = models.IntegerField(default=0)

