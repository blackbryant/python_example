from django.contrib import admin
from myblog.models import Post
from myblog.models import NewTable



class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

class NewTableAdmin(admin.ModelAdmin):
    list_display = ('text_f','date_f')


admin.site.register(Post,PostAdmin)
admin.site.register(NewTable,NewTableAdmin)


