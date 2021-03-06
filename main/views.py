from django.shortcuts import render, redirect
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from django.core.files.storage import FileSystemStorage
import simplejson


def main(request):
    res_data = {}
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        student = request.POST.getlist('student')
        teacher = request.POST.getlist('teacher')

        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'main.html', res_data)
        elif not(student) and not(teacher):
            res_data['error'] = 'CheckBox를 선택해 주세요.'
            return render(request, 'main.html', res_data)
        else:  # 아이디 중복 체크
            try:
                user = User.objects.get(email=email)    # 아이디가 있는지 확인 해보고
            except User.DoesNotExist:   # 아이디가 없어서 DoesNotExist이면 저장한다.
                if student and not(teacher):
                    user = User(email=email, username=username,
                                password=make_password(password), role="student")
                elif teacher and not (student):
                    user = User(email=email, username=username,
                                password=make_password(password), role="teacher")
                user.save()
                return redirect('/login')
            if(user):
                res_data['error'] = '존재하는 Email 입니다.'
                return render(request, 'home.html', res_data)

 # 로그인


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        res_data = {}   # 딕션어리 = key, value 값을 가지는 변수
        if not(email and password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif not(email):
            res_data['error'] = '이메일을 입력하세요.'
        elif not(password):
            res_data['error'] = '비밀번호를 입력하세요.'
        else:
            try:
                user = User.objects.get(email=email)  # 필드명 = 값 이면 user 객체 생성
            except User.DoesNotExist:
                res_data['error'] = '존재하지 않는 아이디 입니다.'    # 아이디가 없는 예외 처리
                return render(request, 'login.html', res_data)

            user_password = user.password
            if check_password(password, user_password):
                request.session['user'] = user.id  # session 변수에 저장
                request.session['user_email'] = user.email  # session 변수에 저장
                return redirect('/home')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
                return render(request, 'login.html', res_data)
        return render(request, 'login.html', res_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


@method_decorator(csrf_exempt, name='dispatch')
def app_login(request):
    # 앱에서 오는 로그인 요청
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        print(email)
        if User.objects.filter(email=email).exists():
            myuser = User.objects.get(email=email)
            # db에서 꺼내는 명령.Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(password, myuser.password):
                return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": myuser.username, "image": str(myuser.image)}))
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
        name = request.POST.get('name', None)
        role = request.POST.get('role', None)

        print(role)
        print(name)
        print(email)
        print(password)
        if User.objects.filter(email=email).exists():
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail", "image": "Fail", "role": "teacher"}))

        else:
            user = User(email=email, password=make_password(
                password), username=name, role=role)
            user.save()
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": name, "image": "yes", "role": "teacher"}))


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
