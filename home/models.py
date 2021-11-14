from django.db import models

class Room(models.Model):
    room_id = models.CharField(max_length=128, verbose_name="방 ID", default=None)
    room_password = models.CharField(max_length=64, verbose_name="방 비밀번호")
    room_name = models.CharField(max_length=128, verbose_name="방 이름")
    file = models.FileField(upload_to="room", verbose_name="파일", default="NULL")
    maker = models.EmailField(max_length=64, verbose_name="생성자", default="NULL")
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    member_list = models.CharField(max_length=64, verbose_name='회원명단리스트',default=None)
    def __str__(self):
        return self.room_name

    class Meta:
        db_table = 'room'
        verbose_name = 'Room 명단'
        verbose_name_plural = 'Room 명단'



class Enrol(models.Model):
    email = models.EmailField(max_length=128, verbose_name="학생")
    room_id = models.CharField(max_length=128, verbose_name="방 ID", default=None)
    room_password = models.CharField(max_length=64, verbose_name="방 비밀번호")
    room_name = models.CharField(max_length=128, verbose_name="방 이름")
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')

    def __str__(self):
        return self.room_id

    class Meta:
        db_table = 'enrol'
        verbose_name = 'enrol 명단'
        verbose_name_plural = 'enrol 명단'

class Analytics(models.Model):
    room_id = models.CharField(max_length=128, verbose_name="방 ID", default="NULL")   
    email = models.EmailField(max_length=128, verbose_name="사용자 email",default="NULL")
    username = models.CharField(max_length=128, verbose_name="사용자 이름",default="NULL")
    count =  models.IntegerField(verbose_name="사용자 수", default=0)
    rate = models.IntegerField(verbose_name="순위", default=0)
    level = models.IntegerField(verbose_name="집중도 레벨",default=0)
    app = models.IntegerField(verbose_name="앱 차단 점수",default=0)    
    person = models.IntegerField(verbose_name="자리 이탈 점수",default=0)
    time = models.IntegerField(verbose_name="학습 시간",default=0)
    list = models.IntegerField(verbose_name="list 변수",default=0)
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'analytics'
        verbose_name = '집중도'
        verbose_name_plural = '집중도'


class Notice(models.Model):
    room_id = models.CharField(max_length=128, verbose_name="방 ID", default="NULL")
    writer = models.EmailField(max_length=128, verbose_name="작성자 email",default="NULL")
    writername = models.CharField(max_length=128, verbose_name="작성자 이름",default="NULL")
    title =  models.CharField(max_length=128, verbose_name="제목",default="NULL")
    description = models.CharField(max_length=1000, verbose_name="내용",default="NULL")
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='작성 날짜')
