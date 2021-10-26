from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from django.core.files.storage import FileSystemStorage
import simplejson

def main(request):
    return render(request, 'main.html')

@method_decorator(csrf_exempt, name='dispatch')
def app_login(request):
    # 앱에서 오는 로그인 요청
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        role = request.POST.get('role',None)
        print(role)
        # 받은 이메일이랑 비밀번호 =데이터와 일치하면
        # 리턴값으로 숫자 200 = 로그인 성공
        # 일치 안하면 숫자 100 = 로그인 실패
        if User.objects.filter(email=email).exists():
            myuser = User.objects.get(email=email)
            # db에서 꺼내는 명령.Post로 받아온 username으로 , db의 username을 꺼내온다.
            if(role==myuser.role):
                if password==myuser.password:
                    print(password)
                    # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                    return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": myuser.username, "image": str(myuser.image)}))
                else:
                    return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail", "image": "Fail"}))
            else:

                return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail", "image": "Fail"}))
        else:
            return HttpResponse(simplejson.dumps({"email": "aa", "password": "aa", "name": "no", "image": "Fail"}))


@method_decorator(csrf_exempt, name='dispatch')
def app_signup(request):

    if request.method == "GET":
        return render(request, 'main/app_signup.html')
    elif request.method == "POST":
        #data = JSONParser().parse(request)
        #serializer = PostSerializer(data=data)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        name = request.POST.get('name'),
        role = request.POST.get('role'),
        print(role)
        print(name)
        print(email)
        print(password)
        if User.objects.filter(email=email).exists():
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail", "image": "Fail","role":"teacher"}))

        else:
            user = User(email=email, password=password, username=name, role=role)
            user.save()
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": name, "image": "yes","role":"teacher"}))          

@method_decorator(csrf_exempt, name='dispatch')
def app_profileimg(request):
    # 프로필 이미지 수정
    if request.method == "POST":
        res_data = {}
        image = request.FILES['image']
        print(image)
        fs = FileSystemStorage()
        res_data['image_url'] = fs.url(image.name)
        print(image.name)

        # 사용자 이메일 구하기
        text = list(image.name)
        del text[len(text)-4:len(text)]
        email = ''.join(text)
        print(email)
        myuser = User.objects.get(email=email)
        myuser.image = image
        myuser.save()
        return HttpResponse("success")


@method_decorator(csrf_exempt, name='dispatch')
def app_getprofileimg(request):
    # 프로필 이미지 수정
    if request.method == "POST":
        email = request.POST.get('email', None)
        myuser = User.objects.get(email=email)
        print(myuser.image)
        return HttpResponse(myuser.image)    