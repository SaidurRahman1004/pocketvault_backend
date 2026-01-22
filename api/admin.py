from django.contrib import admin
from .models import ShoppingItem, Bookmark, MediaItem
#Basic Admin Registrations
'''
admin.site.register(ShoppingItem)
admin.site.register(Bookmark)
admin.site.register(MediaItem)
'''
#Customized Admin Registrations For Better Usability And Orginize View 

@admin.register(ShoppingItem)
class ShoppingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'isBought')
    list_filter = ('category', 'isBought') #Filter Sidebar

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'url')
    search_fields = ('title', 'category') #Search Functionality Box


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'type', 'status', 'rating')
    list_filter = ('type', 'status') #Filter Sidebar
    search_fields = ('title',) #Search Functionality Box
