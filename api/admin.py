from django.contrib import admin

# Register your models here.

from .models import BlogPost, User, Comments

admin.site.register([BlogPost,User,Comments])