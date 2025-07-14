from django.contrib import admin

# Register your models here.
from  .models import Stocks , UserInfo ,  UserStock


admin.site.register(Stocks)
admin.site.register(UserInfo)
admin.site.register(UserStock)