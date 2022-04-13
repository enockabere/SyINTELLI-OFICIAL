from django.contrib import admin
from . models import Category, Offers,caseStudy
from  django.contrib.auth.models  import  Group,User

# Register your models here.

class  AllOffers(admin.ModelAdmin):
    list_display = ('Name','Types','Description','Category')
    search_fields = ('name','types','Category')
    empty_value_display = '-none-'
    list_per_page=25
    
class  CaseAdmin(admin.ModelAdmin):
    list_display = ('title','Description')
    search_fields = ('title',)
    empty_value_display = '-none-'
    list_per_page=25
    
admin.site.register(Category)
admin.site.register(Offers,AllOffers)
admin.site.register(caseStudy,CaseAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)