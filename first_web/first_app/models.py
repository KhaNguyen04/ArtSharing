from django.db import models
from django.contrib.auth.models import User
from accounts.models import *
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserProfile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # email=models.EmailField(max_length=60, unique=True)
    firstName=models.CharField(max_length=25,null=True, blank=True)
    lastName=models.CharField(max_length=25,null=True, blank=True)
    displayName=models.CharField(max_length=30, unique=True,blank=True,)
    about=models.TextField(_('about'),max_length=2000,null=True, blank=True)
    image=models.ImageField(blank=True,null=True)
    last_login=models.DateTimeField(auto_now=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    # city=models.CharField(max_lengt=)
    # country=models.CharField(max_length=)
    def __str__(self):
        return str(self.user)
        
class Category(models.Model):
    category=models.CharField(max_length=30)
    
    def __str__(self):
        return self.category

class Post(models.Model):
    title=models.CharField(max_length=60)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    description=models.CharField(max_length=300, null=True, blank=True)
    likes=models.ManyToManyField(User,default=None,blank=True,related_name='likes')
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return str(self.title)

    # @property
    # def num_like(self):
    #     return self.like.all().count()



#     def __str__(self):
#         return str(self.post)

class Comment(models.Model):
    post=models.ForeignKey(Post,null=True,blank=True,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    comment=models.TextField(max_length=1000)
    date_comment=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id


class Comic(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    post=models.ForeignKey(Post,null=True, on_delete=models.SET_NULL)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    def save(self, *args,**kwargs):
        if self.category is None:
            self.category=self.post.category
        return super().save(*args, **kwargs)

class Chapter(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comic=models.ForeignKey(Comic, on_delete=models.CASCADE)
    title=models.CharField(max_length=60, blank=True)
    chapNumber=models.IntegerField()

# class Strip(models.Model):
#     user=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.id

# class Drawing(models.Model):
#     user=models.ForeignKey(Users,null=True,blank=True,on_delete=models)
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.id

class Photo(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    image = models.ImageField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.id

# class Follows(models.Model):
#     follower_id=models.ForeignKey(Users,null=True,blank=True,on_delete=models)
#     followee_id=models.ForeignKey(Users,null=True,blank=True,on_delete=models)
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.id



# class Contact(models.Model):
#     type=models.Charfield(max_length=30,blank=True)
#     link=models.CharField(max_length=2000,blank=True)
#     def __str__(self):
#         return self.id

class Like(models.Model):
    LIKE_CHOICES= (
    ('Like','Like'),
    ('Unlike','Unlike'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default="",max_length=10)

