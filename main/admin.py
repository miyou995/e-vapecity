from django.contrib import admin
from .models import Product, SubCategory, Category, TreeCategory
from django.contrib.auth.models import Group, User

# Register your models here.
admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.unregister(Group)
# admin.site.unregister(User)

class TreeLinesAdmin(admin.TabularInline):
    model = TreeCategory
    readonly_fields = ('name','slug')
    # fields = ('name',)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name')
    list_per_page = 40
    list_filter = ('name', 'slug')
    # list_editable = ['name']
    search_fields = ('id', 'name',)
    exlude = ['slug']
    inlines = [TreeLinesAdmin,]


class TreeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 40
    list_filter = ('name', 'category')
    list_editable = ['category']
    search_fields = ('name','category')
    exlude = ['slug']




class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'tree')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 40
    list_filter = ('name', 'tree')
    list_editable = ['tree']
    search_fields = ('name','tree')
    exlude = ['slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'sous_category','price', 'new', 'top', 'available')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 40
    list_filter = ('name', 'sous_category','price', 'new')
    list_editable = ['sous_category','price', 'new', 'top', 'available']
    search_fields = ('name','price')
    exlude = ['slug']
    save_as = True


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(TreeCategory, TreeCategoryAdmin)
