from django.contrib import admin
from .models import Post1, Home, Category, Tags, Contact


# Register your models here.

class Post1Admin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)


admin.site.register(Post1, Post1Admin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Contact)