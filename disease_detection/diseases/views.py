from django.shortcuts import render

# Create your views here.
import os
import joblib
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'index.html')

def diabetes(request):
    return render(request, 'diabetes.html')

def heart(request):
    return render(request, 'heart.html')

def parkinsons(request):
    return render(request, 'parkinsons.html')

def result_diabetes(request):
    model = joblib.load('diabetes_model.sav')
    lis = []
    lis.append(request.POST['pregnancies'])
    lis.append(request.POST['glucose'])
    lis.append(request.POST['bloodpressure'])
    lis.append(request.POST['skinthickness'])
    lis.append(request.POST['insulin'])
    lis.append(request.POST['bmi'])
    lis.append(request.POST['diabetespedigreefunction'])
    lis.append(request.POST['age'])
    lis = np.array(lis)
    lis = lis.reshape(1, -1)
    ans = model.predict(lis)
    if ans[0] == 1:
        return render(request, 'result_diabetes.html', {'result': 'You have diabetes'})
    else:
        return render(request, 'result_diabetes.html', {'result': 'You do not have diabetes'})
    
def result_heart(request):
    model = joblib.load('heart_model.sav')
    lis = []
    lis.append(request.POST['age'])
    lis.append(request.POST['sex'])
    lis.append(request.POST['cp'])
    lis.append(request.POST['trestbps'])
    lis.append(request.POST['chol'])
    lis.append(request.POST['fbs'])
    lis.append(request.POST['restecg'])
    lis.append(request.POST['thalach'])
    lis.append(request.POST['exang'])
    lis.append(request.POST['oldpeak'])
    lis.append(request.POST['slope'])
    lis.append(request.POST['ca'])
    lis.append(request.POST['thal'])
    lis = np.array(lis)
    lis = lis.reshape(1, -1)
    ans = model.predict(lis)
    if ans[0] == 1:
        return render(request, 'result_heart.html', {'result': 'You have heart disease'})
    else:
        return render(request, 'result_heart.html', {'result': 'You do not have heart disease'})
    
def result_parkinsons(request):
    model = joblib.load('parkinsons_model.sav')
    lis = []
    lis.append(request.POST['fo'])
    lis.append(request.POST['fhi'])
    lis.append(request.POST['flo'])
    lis.append(request.POST['jitter'])
    lis.append(request.POST['jitterinabs'])
    lis.append(request.POST['rap'])
    lis.append(request.POST['ppq'])
    lis.append(request.POST['ddp'])
    lis.append(request.POST['shimmer'])
    lis.append(request.POST['shimmerindB'])
    lis.append(request.POST['apq3'])
    lis.append(request.POST['apq5'])
    lis.append(request.POST['apq'])
    lis.append(request.POST['dda'])
    lis.append(request.POST['nhr'])
    lis.append(request.POST['hnr'])
    lis.append(request.POST['rpde'])
    lis.append(request.POST['dfa'])
    lis.append(request.POST['spread1'])
    lis.append(request.POST['spread2'])
    lis.append(request.POST['d2'])
    lis.append(request.POST['ppe'])
    lis = np.array(lis)
    lis = lis.reshape(1, -1)
    ans = model.predict(lis)
    if ans[0] == 1:
        return render(request, 'result_parkinsons.html', {'result': 'You have Parkinsons disease'})
    else:
        return render(request, 'result_parkinsons.html', {'result': 'You do not have Parkinsons disease'})
    

def dengue(request):
    return render(request, 'dengue.html')

def result_dengue(request):
    model = joblib.load('dengue_model.sav')
    lis = []
    lis.append(request.POST['tempmax'])
    lis.append(request.POST['tempmin'])
    lis.append(request.POST['temp'])
    lis.append(request.POST['feelslikemax'])
    lis.append(request.POST['feelslikemin'])
    lis.append(request.POST['feelslike'])
    lis.append(request.POST['dew'])
    lis.append(request.POST['humidity'])
    lis.append(request.POST['precip'])
    lis.append(request.POST['precipprob'])
    lis.append(request.POST['precipcover'])
    lis.append(request.POST['snow'])
    lis.append(request.POST['snowdepth'])
    lis.append(request.POST['windspeed'])
    lis.append(request.POST['winddir'])
    lis.append(request.POST['sealevelpressure'])
    lis.append(request.POST['cloudcover'])
    lis.append(request.POST['visibility'])
    lis.append(request.POST['solarradiation'])
    lis.append(request.POST['solarenergy'])
    lis.append(request.POST['uvindex'])
    lis.append(request.POST['conditions'])
    lis.append(request.POST['stations'])
    lis.append(request.POST['cases'])
    lis = np.array(lis)
    lis = lis.reshape(1, -1)
    ans = model.predict(lis)
    if ans[0] == 1:
        return render(request, 'result_dengue.html', {'result': 'You have Dengue'})
    else:
        return render(request, 'result_dengue.html', {'result': 'You do not have Dengue'})

def signup_login(request):
    return render(request, 'signup_login.html')

def aboutus(request):
    return render(request, 'aboutus.html')


