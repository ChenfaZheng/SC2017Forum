from django.contrib import admin
from .models import Poster


# class ReviewInline(admin.TabularInline):
#     model = Review


class PosterAdmin(admin.ModelAdmin):
    # inlines = [
    #     ReviewInline, 
    # ]
    list_display = (
        "title", 
        "author", 
    )


admin.site.register(Poster, PosterAdmin)