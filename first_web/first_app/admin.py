from django.contrib import admin
from .models import *
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('id','user','firstName', 'lastName','displayName',)
    ordering=('id',)
    search_fields=('id','name','display')
    # user.short_description='username'


class CategoryAdmin(admin.ModelAdmin):
    list_display=('category','id',)
    ordering=('id',)
    search_fields=('category',)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','category','user','date_created')
    ordering=('-date_created',)
    search_fields=('title','category','user')


class CommentAdmin(admin.ModelAdmin):
    list_display=('post','user','date_comment')
    ordering=('-date_comment',)
    search_fields=('post','user')


class ComicAdmin(admin.ModelAdmin):
    list_display=('post','user','category','created_at')
    ordering=('post',)
    search_fields=('post','user')

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
# admin.site.register(Like)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Comic,ComicAdmin)