from django.contrib import admin
from .models import Post

admin.site.register(Post) # 관리자 페이지에서 만든 모델을 보려면 이 함수로 모델을 등록해야함.