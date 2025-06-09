from django.contrib import admin
from django.urls import path, include
from blog.views import *
# 만약 import blog.views <- 이렇게 되어 있는 분들은 그대로 진행해주세요!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]