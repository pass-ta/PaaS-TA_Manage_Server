from django.shortcuts import render
from django.http import HttpResponse

from django.db.models.fields import NullBooleanField
from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import redirect, render
from django.urls.conf import path
from main.models import User
from .models import Room
import string, random
from django.views.generic import ListView
from collections import OrderedDict
# from .fusioncharts import FusionCharts
import base64

import simplejson
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers

import os
import base64
# from luxand import luxand
# from openpyxl import load_workbook
# from openpyxl_image_loader import SheetImageLoader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@method_decorator(csrf_exempt, name='dispatch')
def app_enterroom(request):
    # 앱에서 오는 로그인 요청
    if request.method == "POST":
        roomname = request.POST.get('roomname', None)
        password = request.POST.get('password', None)
        # 받은 이메일이랑 비밀번호 =데이터와 일치하면
        # 리턴값으로 숫자 200 = 로그인 성공
        # 일치 안하면 숫자 100 = 로그인 실패
        if Room.objects.filter(class_name=roomname).exists():
            room = Room.objects.get(class_name=roomname)
            # db에서 꺼내는 명령.Post로 받아온 username으로 , db의 username을 꺼내온다.
            print(password)
            print(room.class_name)
            if password == room.class_password:
                print(room.class_password)
                # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                # room_type(exam mode, study mode)구분해서 들고오기
                return HttpResponse("success")
            else:
                # 방 비번 불일치
                return HttpResponse("fail")

        else:
            # 방 없음
            return HttpResponse("NoRoom")

@method_decorator(csrf_exempt, name='dispatch')
def app_attendance(request):
    if request.method == "POST":
        info = {}
        # change_here
        room_name = request.POST.get('room', None)
        member_name = request.POST.get('name', None)
        member_number = request.POST.get('number', None)

        print(room_name)
        print(member_name)
        print(member_number)
        # room DB-member_list로 회원번호 확인 및 index 추출
        room = Room.objects.get(class_name=room_name)
        # member_list = room.member_list  # 회원번호만 적힌 리스트
        # member_list = member_list[1:-1].split(', ')
        # print(member_list)

        # CHECK NUMBER
        # Correct NUMBER
        # if (member_number in member_list):
        #     member_index = member_list.index(member_number) + 1
        #     print('member_index:'+str(member_index))

        #     # 해당방의 DB속 명단Excel파일 조회
        #     room = Room.objects.get(room_name=room_name)
        #     member_file = room.file  # 명단

        #     member = load_workbook("media/" + str(member_file))
        #     sheet = member['Sheet1']
        #     member_file_name = sheet['B'+str(member_index)].value

        #     # CHECK NAME
        #     # Wrong NAME
        #     if member_file_name != member_name:
        #         print('app_enterEXAM_info_no_match_name_num')
        #         return HttpResponse(simplejson.dumps({"roomname": "no",  "password": "no"}))
        #     # Correct NAME
        #     else:
        #         print('app_enterEXAM_info_success')
        #         return HttpResponse(simplejson.dumps({"roomname": "yes", "password": member_index}))

        # # Wrong NUMBER
        # else:
        #     print('app_enterEXAM_info_no_num')
        #     return HttpResponse(simplejson.dumps({"roomname": "fail", "password": "no"}))

        return HttpResponse("success")

@method_decorator(csrf_exempt, name='dispatch')
def app_checkimg(request):
    if request.method == "POST":
        # APP : 캡쳐이미지 받기
        capture_image = request.FILES['image']
        print(capture_image)
        # image.name = <room_name>_<member_number>_capture.png
        fs = FileSystemStorage()
        filename = fs.save("capture/"+capture_image.name, capture_image)
        uploaded_file_url = fs.url(filename)
        print(filename)
        print(uploaded_file_url)

        # image.name 에서 분리
        l = capture_image.name.split('_')
        room_name = l[0]
        member_index = l[1]

        print("Get All DATA ")

        # # Room DB - excel 파일
        # room = Room.objects.get(room_name=room_name)
        # member_file = room.file  # 명단
        # member = load_workbook("media/" + str(member_file))
        # sheet = member['Sheet1']

        # # exel 명단 속 이미지
        # image_loader = SheetImageLoader(sheet)
        # image = image_loader.get('C'+str(member_index))
        # member_file_image_path = (room_name+"_"+str(member_index)+".jpg")
        # image.save("media/capture/"+member_file_image_path)
        # fs = FileSystemStorage()

        # # Face Recognition
        # a = (fs.location + str("/capture/") + member_file_image_path)
        # b = (fs.location + str("/capture/") + capture_image.name)
        # # luxand API
        # luxand_client = luxand("12a42a8efedf4e24b84730ce440e5429")
        # member_file_image = luxand_client.add_person(
        #     str(member_index), photos=[a])
        # result = luxand_client.verify(member_file_image, photo=b)
        # print(result)
        # os.remove(os.path.join(settings.MEDIA_ROOT +
        #                        "/capture/", capture_image.name))
        # # Recognition RESULT
        # if result['status'] == 'success':
        #     print("Recognition_SUCCESS")
        #     return HttpResponse(simplejson.dumps({"image": "ok"}))  # 이미지 전송완료
        # else:
        #     print("Recognition_FAIL")
        #     return HttpResponse(simplejson.dumps({"image": "no"}))  # 이미지 전송실패

        return HttpResponse("success")