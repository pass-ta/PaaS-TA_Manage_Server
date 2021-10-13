
from django.db import models
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage



# 이미지 overwrite

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=128, verbose_name="이메일")
    username = models.CharField(max_length=64, verbose_name="이름")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registerd_date = models.DateTimeField(
        auto_now_add=True, verbose_name='가입시간')
    image = models.ImageField(
        default="face-recognition.png", verbose_name='이미지', storage=OverwriteStorage())
    role = models.CharField(max_length=10, verbose_name="신분")        # teacher, student
    check = models.BooleanField(default=False)        # 앱 인증 완료시 true

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        verbose_name = '사용자 명단'
        verbose_name_plural = '사용자 명단'  # 복수명 설정