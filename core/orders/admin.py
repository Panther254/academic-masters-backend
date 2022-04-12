from django.contrib import admin
from .models import Order,Urgency,Subject,MediaFiles
# Register your models here.


admin.site.register(Order)
admin.site.register(Urgency)
admin.site.register(Subject)
admin.site.register(MediaFiles)
