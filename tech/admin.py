from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.Contact)
admin.site.register(models.Appli)
admin.site.register(models.contactus)
admin.site.register(models.pay)
admin.site.register(models.Provisional)
admin.site.register(models.InqueryForm)
admin.site.register(models.about_s)
admin.site.register(models.comment)
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=['name','photo']

