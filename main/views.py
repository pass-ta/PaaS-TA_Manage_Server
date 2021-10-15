from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
import simplejson


@method_decorator(csrf_exempt, name='dispatch')
def app_login(request):
    # 앱에서 오는 로그인 요청
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        role = request.POST.get('role',None)
        # 받은 이메일이랑 비밀번호 =데이터와 일치하면
        # 리턴값으로 숫자 200 = 로그인 성공
        # 일치 안하면 숫자 100 = 로그인 실패
        if User.objects.filter(email=email).exists():
            myuser = User.objects.get(email=email)
            # db에서 꺼내는 명령.Post로 받아온 username으로 , db의 username을 꺼내온다.
            if(role==myuser.role):
                if check_password(password,myuser.password):
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

    if request.method == "POST":
        #data = JSONParser().parse(request)
        #serializer = PostSerializer(data=data)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        name = request.POST.get('name', None),
        role = request.POST.get('role', None),
        print(role)
        print(name)
        print(email)
        if User.objects.filter(email=email).exists():
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail", "image": "Fail"}))

        else:
            user = User(email=email, password=make_password(
                password), username=name, role=role)
            user.save()
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": name, "image": str(user.image)}))          