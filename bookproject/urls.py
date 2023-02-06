from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/',include('accounts.urls')), #機能の呼び出し。accountsアプリに、ログイン・ログアウト機能をまとめる。
    path('',include('book.urls')),
]

# 画像とURLとを結ぶ処理
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)