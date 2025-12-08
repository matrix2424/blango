from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post, Comment, AuthorProfile
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(AuthorProfile)

# Register your models here.
admin.site.register(Comment)
