from django.contrib import admin
from myblog.models import Post
from myblog.models import NewTable
from myblog.models import Product


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

class NewTableAdmin(admin.ModelAdmin):
    list_display = ('text_f','date_f')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','size')


admin.site.register(Post,PostAdmin)
admin.site.register(NewTable,NewTableAdmin)
admin.site.register(Product,ProductAdmin)

