import io
import os
import pickle

import imagine as imagine
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages
from deplom.forms import *
from tasks.models import *
import numpy as np
from PIL import Image
import tensorflow as tf

def index(request):
    return render(request, "index.html")

def signin(request):
    return render(request, "tasks.html")

def info(request):
    return render(request, "info.html")

def news(request):
    return render(request, "news.html")

def work(request):
    return render(request, "work.html")

def workphoto1(request):
    return render(request, "workphoto1.html")

def workphoto2(request):
    return render(request, "workphoto2.html")

def tasks(request):




    '''image = tf.image.decode_png(byte_array, channels=3, dtype=tf.uint8)
    width = image.shape[1]
    height = image.shape[0]

    # Сохраняем изображение, указав размер
    tf.keras.utils.save_img(
        'static/image/my_image.png',
        image,
        scale=False,
        dpi=(width, height)
    )'''



    obj = Tasks.objects.order_by("id_brigade")
    tt = TypeTask.objects.first()
    pl = Place.objects.all()
    hw = Highways.objects.all()
    use = request.user.username
    worker = Workers.objects.get(login=use)



    img_bate = worker.photo
    img_bate = pickle.dumps(img_bate)

    img = np.frombuffer(img_bate, dtype=np.uint8)

    im = Image.fromarray(img)

    if os.path.exists('static/image/my_image.png'):
        os.remove('static/image/my_image.png')
        im.save('static/image/my_image.png', format='PNG')
    else:
        im.save('static/image/my_image.png', format='PNG')
    return render(request, "tasks.html", {"obj": obj, "worker": worker, "tt": tt, "pl": pl, "hw": hw, "img": im, "IMG": img_bate})






def test(request):
    obj = Users.objects.order_by("id_role")
    use = request.user.username
    worker = Workers.objects.get(login=use)
    return render(request, "test.html", {"obj": obj, "worker": worker})

def login_user(request):
    context = {'login_form': LoginForm()}

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'Пользователь с логином {username} и пароль не был найден!'
                }
        else:
            context = {
                'login_form': login_form,
            }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')