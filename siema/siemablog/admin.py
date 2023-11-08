from django.contrib import admin
from .models import Post, Material, Comic, Quiz, UserActivity

admin.site.register(UserActivity)
admin.site.register(Post)
admin.site.register(Material)
admin.site.register(Comic)
admin.site.register(Quiz)
