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