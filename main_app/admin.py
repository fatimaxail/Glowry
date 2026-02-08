from django.contrib import admin
from .models import Profile, Article, Review, Routine, RoutineProduct

# Register your models here.
admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(Review)
admin.site.register(Routine)
admin.site.register(RoutineProduct)
