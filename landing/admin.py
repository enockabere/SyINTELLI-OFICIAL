from django.contrib import admin
from . models import Category, Offers,caseStudy, Culture,Mission
from  django.contrib.auth.models  import  Group,User
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class AllOffers(SummernoteModelAdmin):
    list_display = ('Name','Types','Description','Category')
    search_fields = ('name','types','Category')
    list_display_links = ['Name', 'Category']
    empty_value_display = '-none-'
    list_per_page=25
    
class CaseAdmin(SummernoteModelAdmin):
    list_display = ('title','Description')
    list_display_links = ['title']
    search_fields = ('title',)
    empty_value_display = '-none-'
    list_per_page=25
class CultureAdmin(SummernoteModelAdmin):
    list_display = ('title','Content','date_added')
    list_display_links = ['title']
    search_fields = ('title',)
    empty_value_display = '-none-'
    list_per_page=25
    
class MissionAdmin(SummernoteModelAdmin):
    list_display = ('title','Content','date_added')
    list_display_links = ['title']
    search_fields = ('title',)
    empty_value_display = '-none-'
    list_per_page=25

    
admin.site.register(Category)
admin.site.register(Offers,AllOffers)
admin.site.register(caseStudy,CaseAdmin)
admin.site.register(Culture,CultureAdmin)
admin.site.register(Mission,MissionAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)