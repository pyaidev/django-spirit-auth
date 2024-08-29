from django.contrib import admin
from .models import SiteUser, Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    fields = ('name', 'code')
    
    
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    fields = ('name', 'country')





@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'email', 'last_visit', 'rating', 'order_counts', 'disput_counts', 'win_disputs', 'block')
    fields = ('username', 'display_name', 'email', 'last_visit', 'rating', 'order_counts', 'disput_counts', 'win_disputs', 'note', 'country', 'city', 'user_avatar', 'block', 'block_comment')
