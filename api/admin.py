from django.contrib import admin
from api.models import User, Article, ArticleTag, Comment, Like, Follow

# Register your models here.
admin.site.register(User)
admin.site.register(Article)
admin.site.register(ArticleTag)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
