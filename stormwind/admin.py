from django.contrib import admin
from .models import Thread,Category,Reply

admin.site.register(Thread)
admin.site.register(Category)
admin.site.register(Reply)