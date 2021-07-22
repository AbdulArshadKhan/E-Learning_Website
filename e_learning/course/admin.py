from django.contrib import admin
from .models import Video,Author,User,Student
# Register your models here.

admin.site.register(Video)
admin.site.register(Author)
admin.site.register(User)
admin.site.register(Student)