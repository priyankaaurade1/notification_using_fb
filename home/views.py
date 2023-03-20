

from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests
import firebase_admin
from firebase_admin import messaging
from notification_app.settings import FIREBASE_CONFIG

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .forms import createUserForm
from django.contrib.auth.forms import UserCreationForm
def login(request):
    context = {

    }
    return render(request, 'login.html',context)

def register(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form' : form
    }
    return render(request, 'register.html',context)

@csrf_exempt
def fcm_endpoint(request):
    if request.method == 'POST':
        # Extract notification data from request
        data = request.POST.get('data', {})
        token = request.POST.get('token', '')
        
        # Send notification using Firebase Cloud Messaging API
        headers = {
            'Authorization': 'key=YOUR_SERVER_KEY',
            'Content-Type': 'application/json'
        }
        payload = {
            'to': token,
            'data': data
        }
        response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, json=payload)
        
        # Return response to Firebase
        return HttpResponse(response.content, content_type='application/json')
    else:
        return HttpResponse(status=405)

# def send_notification(request):
#     if request.method == 'POST':
#         # Get the form data
#         title = request.POST['title']
#         body = request.POST['body']

#         # Construct the message
#         message = messaging.Message(
#             notification=messaging.Notification(
#                 title=title,
#                 body=body,
#             ),
#             topic='test_topic',
#         )

#         # Send the message
#         response = messaging.send(message)

#         # Render the response
#         return render(request, 'index.html', {'response': response})

#     return render(request, 'index.html')












# ======================================================================================================================

# from django.http.request import HttpHeaders
# from django.shortcuts import render

# from django.http import HttpResponse
# import requests
# import json
# # Create your views here.

# def index(request):
#     return render(request,'index.html')

# def showFirebaseJS(request):
#     data =  'importScripts("https://www.gstatic.com/firebasejs/9.18.0/firebase-app.js");'\
#             'importScripts("https://www.gstatic.com/firebasejs/9.18.0/firebase-analytics.js");'\
#             'var firebaseConfig = {' \
#             '        apiKey: "AIzaSyBePUakyUc3O2D3F47sa2FMHWIIxI3QMBc",' \
#             '        authDomain: "notification-f3d49.firebaseapp.com",' \
#             '        databaseURL: "databaseURL: "https://notification-f3d49-default-rtdb.firebaseio.com",' \
#             '        projectId: "notification-f3d49",' \
#             '        storageBucket: "notification-f3d49.appspot.com",' \
#             '        messagingSenderId: "461663820899",' \
#             '        appId: "1:461663820899:web:139ba3d6a794ea784d2c56",' \
#             '        measurementId: "G-1WR6S4WH7D"' \
#             ' };' \
#             'firebase.initializeApp(firebaseConfig);' \
#             'const messaging=firebase.messaging();' \
#             'messaging.setBackgroundMessageHandler(function (payload) {' \
#             '    console.log(payload);' \
#             '    const notification=JSON.parse(payload);' \
#             '    const notificationOption={' \
#             '        body:notification.body,' \
#             '        icon:notification.icon' \
#             '    };' \
#             '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
#             '});'
#     print('===================',data)
#     return HttpResponse(data,content_type="text/javascript")