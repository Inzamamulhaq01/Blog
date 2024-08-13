from django.contrib import admin
from .models import Post,about,Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(about)
admin.site.register(Comment)

