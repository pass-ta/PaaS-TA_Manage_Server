from django.shortcuts import render
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from main.models import User

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
            return render(request, 'home.html', res_data)
        elif request.method == 'POST':
            userimage = request.FILES['user-img-change']
            res_data['userimg'] = fs.url(userimage)
            user.image = userimage
            user.save()
            res_data['img_check'] = 1
            return render(request, 'home.html', res_data)
    else:
        return redirect('/login')
