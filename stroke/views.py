from django.shortcuts import render
from django.http import JsonResponse
from .models import PredResults

import pandas as pd 
import pickle

def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):
    if request.POST.get('action') == 'post':
        #réception des données du client 

        gender = float(request.POST.get('gender'))
        age = float(request.POST.get('age'))
        hypertension = float(request.POST.get('hypertension'))
        heart_disease = float(request.POST.get('heart_disease'))
        ever_married = float(request.POST.get('ever_married'))
        work_type = float(request.POST.get('work_type'))
        residence_type = float(request.POST.get('residence_type'))
        avg_glucose_level = float(request.POST.get('avg_glucose_level'))
        bmi = float(request.POST.get('bmi'))
        smoking_status = float(request.POST.get('smoking_status'))
        


        # model = pd.read_pickle(r"/home/chadha/Desktop/django_projects/stroke_prediction/stroke_prediction/model_prediction.sav")
        filename = r"/home/chadha/Desktop/django_projects/stroke_prediction/stroke_prediction/model_prediction.sav"
        model = pickle.load(open(filename, 'rb'))
        result = model.predict([[gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]])

        classification = result[0]

        PredResults.objects.create(gender=gender, age = age, hypertension=hypertension, heart_disease=heart_disease, ever_married=ever_married,
        work_type=work_type, residence_type=residence_type, avg_glucose_level=avg_glucose_level, bmi=bmi, smoking_status=smoking_status, classification=classification)

        return JsonResponse({'result': classification, 'gender': gender, 'age': age, 'hypertension': hypertension, 'heart_disease': heart_disease, 'ever_married': ever_married, 'work_type': work_type, 'residence_type':residence_type, 'avg_glucose_level': avg_glucose_level, 'bmi': bmi, 'smoking_status': smoking_status}, safe = False)

def view_results(request):
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)