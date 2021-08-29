from django.contrib import admin
from .models import UserProfile, Company, Comment

class UserProfileAdmin(admin.ModelAdmin):
    pass

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class CompanyAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Company, CompanyAdmin)