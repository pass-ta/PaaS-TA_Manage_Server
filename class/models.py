from django.db import models
from django.conf import settings
import os

class Room(models.Model):
    class_name = models.CharField(max_length=128, verbose_name="수업 이름")
    class_password = models.CharField(max_length=64, verbose_name="수업 비밀번호")
    teacher = models.EmailField(max_length=64, verbose_name="교사", default="NULL")
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    student_list = models.CharField(max_length=64, verbose_name='학생명단리스트',default=None)
    # file = models.FileField(upload_to="room", verbose_name="파일", default="NULL")
    def __str__(self):
        return self.class_name

    class Meta:
        db_table = 'class'
        verbose_name = 'class 명단'
        verbose_name_plural = 'class 명단'
