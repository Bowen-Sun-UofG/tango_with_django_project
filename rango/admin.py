from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')  # ✅ 添加这个

admin.site.register(Category)
admin.site.register(Page, PageAdmin)  # ✅ 这样 Page 在 Admin 里会显示正确的列
