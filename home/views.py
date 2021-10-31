from django.shortcuts import render
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from main.models import User
import string, random

from home.models import Room
import os
import base64
from luxand import luxand
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader
from HiClass import settings

def home(request):
    res_data = {}
    user_session = request.session.get('user')              # 로그인 체크
    fs = FileSystemStorage()
    if user_session:
        user = User.objects.get(pk=user_session)
        res_data['username'] = user.username                # mypage 정보
        res_data['email'] = user.email
        res_data['register'] = user.registerd_date
        res_data['userimg'] = fs.url(user.image)

        if res_data['userimg'] == "/media/":               # 이미지 체크
            res_data['img_check'] = 0                      # 이미지 널
        else:
            res_data['img_check'] = 1
             
        if request.method == 'GET':
            if user.role == 'student':
                return render(request, 'home-s.html', res_data)
            else:
                return render(request, 'home.html', res_data)
        elif request.method == 'POST':
            userimage = request.FILES['user-img-change']
            res_data['userimg'] = fs.url(userimage)
            user.image = userimage
            user.save()
            res_data['img_check'] = 1
            if user.role == 'student':
                return render(request, 'home-s.html', res_data)
            else:
                return render(request, 'home.html', res_data)
    else:
        return redirect('/login')


def makeclass(request):
    res_data = {}
    user_session = request.session.get('user')
    fs = FileSystemStorage()
    if user_session:
        user = User.objects.get(pk=user_session)            # 로그인 체크
        res_data['username'] = user.username                # mypage 정보
        res_data['email'] = user.email
        res_data['register'] = user.registerd_date
        res_data['string'] = ''.join(random.choice(
            string.ascii_uppercase + string.digits)for _ in range(7))  # 랜덤 문자열 생성
        res_data['userimg'] = fs.url(user.image)

        if res_data['userimg'] == "/media/":               # 이미지가 있는지 체크
            res_data['img_check'] = 0
        else:
            res_data['img_check'] = 1

        if request.method == 'GET':
            return render(request, 'makeroom.html', res_data)
        elif request.method == 'POST':
            room_id = request.POST.get('room-id', None)
            room_password = request.POST.get('room-password', None)
            room_name = request.POST.get('room-name', None)
            maker = user.email
            member_list=[]
        
            try:
                file = request.FILES['file']
            except:
                file = "NULL"

            #학생명단 file
            #명단에서학번만 추출
            if not(file == "NULL"):
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                member = load_workbook("media/" + file.name)
                for cell in member['Sheet1']['A']:
                    member_list.append(cell.value)
                
                os.remove(os.path.join(settings.MEDIA_ROOT, file.name))
           
        
            if not(room_password):
                res_data['password_error'] = '비밀번호를 생성해 주세요.'
            elif (not(room_name)):
                res_data['name_error'] = 'Class의 이름을 적어 주세요.'
            elif (file=="NULL"):
                res_data['file_error'] = '출석부를 첨부 해주세요.'
            else:
                room = Room(room_id=room_id,room_password=room_password,room_name=room_name,
                            file=file,maker=maker, member_list = member_list)  # db에 room 정보 저장
                room.save()
                request.session['room_name'] = room_name # 방을 성공적으로 만들면 room_name으로 room_session을 저장
                return redirect('/home/makeclass/success')
            # room 정보 비정상 일시
            return render(request, 'makeroom.html', res_data)
    else:
        return redirect('/login')

def make_success(request):
    res_data = {}
    fs = FileSystemStorage()
    room_session = request.session.get('room_name')   # 아까 POST 할때 session에 저장한 값 불러옴
    user_session = request.session.get('user')
    if room_session and user_session:
        user = User.objects.get(pk=user_session)    # 로그인 체크
        res_data['username'] = user.username        # mypage 정보
        res_data['email'] = user.email
        res_data['register'] = user.registerd_date

        # 가장 최근의 room_name과 session에 저장한 것을 비교함
        room = Room.objects.get(room_name=room_session)
        res_data['room_id'] = room.room_id
        res_data['room_name'] = room.room_name
        res_data['room_password'] = room.room_password
        res_data['maker'] = room.maker

        res_data['userimg'] = fs.url(user.image)

        if res_data['userimg'] == "/media/":               # 이미지 체크
            res_data['img_check'] = 0
        else:
            res_data['img_check'] = 1
        if request.method == 'GET':
            return render(request, 'make_success.html', res_data)
        elif request.method == 'POST':
            if room.mode == "EXAM":
                return redirect('/main/enteroom/exam1')
            elif room.mode == "STUDY":
                return redirect('/main/enteroom/study1')
    else:
        return redirect('/login')
