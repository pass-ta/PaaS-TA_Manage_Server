from django.db import models


class Room(models.Model):
    room_id = models.CharField(
        max_length=128, verbose_name="방 아이디", default=None)
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


class Quiz(models.Model):
    id = models.AutoField(verbose_name="질문 아이디", primary_key=True)
    maker = models.CharField(max_length=64, verbose_name='생성자', null=True)
    room_id = models.CharField(
        max_length=128, verbose_name="방 아이디", default=None)
    question = models.CharField(max_length=64, verbose_name='질문')
    item1 = models.CharField(max_length=128, verbose_name='질문지1')
    item2 = models.CharField(max_length=128, verbose_name='질문지2')
    item3 = models.CharField(max_length=128, verbose_name='질문지3')
    item4 = models.CharField(max_length=128, verbose_name='질문지4')
    answer = models.IntegerField(verbose_name='정답', default=None)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'Quiz'
        verbose_name = 'Quiz 명단'
        verbose_name_plural = 'Quiz 명단'
