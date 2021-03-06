from django.db import models


class Room(models.Model):
    room_id = models.CharField(max_length=128, verbose_name="방 ID", default=None)
    room_password = models.CharField(max_length=64, verbose_name="방 비밀번호")
    room_name = models.CharField(max_length=128, verbose_name="방 이름")
    file = models.FileField(
        upload_to="room", verbose_name="파일", default="NULL")
    maker = models.EmailField(
        max_length=64, verbose_name="생성자", default="NULL")
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    member_list = models.CharField(
        max_length=64, verbose_name='회원명단리스트', default=None)

    def __str__(self):
        return self.room_id

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
    level = models.IntegerField(verbose_name="집중도 레벨",default=0)
    app = models.IntegerField(verbose_name="앱 차단 점수",default=0)    
    person = models.IntegerField(verbose_name="자리 이탈 점수",default=0)
    quiz = models.IntegerField(verbose_name="퀴즈 점수",default=0)
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
    class Meta:
        db_table = 'notice'
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'


class Quiz(models.Model):
    id = models.AutoField(verbose_name="질문 아이디", primary_key=True)
    maker = models.EmailField(max_length=64, verbose_name='생성자 이메일', null=True)
    makername = models.CharField(max_length=128, verbose_name="생성자 이름",default="NULL")
    room_id = models.CharField(
        max_length=128, verbose_name="방 아이디", default=None)
    question = models.CharField(max_length=64, verbose_name='질문')
    item1 = models.CharField(max_length=128, verbose_name='질문지1')
    item2 = models.CharField(max_length=128, verbose_name='질문지2')
    item3 = models.CharField(max_length=128, verbose_name='질문지3')
    item4 = models.CharField(max_length=128, verbose_name='질문지4')
    answer = models.IntegerField(verbose_name='정답', default=None)
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'Quiz'
        verbose_name = 'Quiz 명단'
        verbose_name_plural = 'Quiz 명단'


class SolvedQuiz(models.Model):
    id = models.AutoField(verbose_name="질문 아이디", primary_key=True)
    user = models.EmailField(max_length=64, verbose_name='사용자 이메일', null=True)
    makername = models.CharField(max_length=128, verbose_name="생성자 이름",default="NULL")
    room_id = models.CharField(max_length=128, verbose_name="방 아이디", default=None)
    question = models.CharField(max_length=64, verbose_name='질문', default='aaa')
    item1 = models.CharField(max_length=128, verbose_name='질문지1', default='aaa')
    item2 = models.CharField(max_length=128, verbose_name='질문지2', default='aaa')
    item3 = models.CharField(max_length=128, verbose_name='질문지3', default='aaa')
    item4 = models.CharField(max_length=128, verbose_name='질문지4', default='aaa')
    answer = models.IntegerField(verbose_name='정답', default='0')
    make_date = models.DateTimeField(auto_now_add=True, verbose_name='학습 날짜')

    class Meta:
        db_table = 'SolvedQuiz'
        verbose_name = '학습한 Quiz'
        verbose_name_plural = '학습한 Quiz'
