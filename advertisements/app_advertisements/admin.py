from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'image_thumbnail']
    list_filter = ['price', 'created_at', 'updated_at', 'auction']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общие', {'fields': ('title', 'description', 'image', 'user')}),
        ('Финансы', {'fields': ('price', 'auction')})#, 'classes': ['collapse']})
    )
     
    
    
    
    
    
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display(description='Изображение')
    def image_thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))




admin.site.register(Advertisement, AdvertisementAdmin)
  