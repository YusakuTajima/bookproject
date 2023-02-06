'''
管理画面を管理しているファイル
'''
from django.contrib import admin
from .models import Book , Review
# from .models import SampleModel


# admin.site.register(SampleModel)
admin.site.register(Book) #管理画面に「Book」を表示させるもの
admin.site.register(Review) #Reviewも管理画面に表示させる