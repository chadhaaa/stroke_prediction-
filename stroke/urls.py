from django.urls import path
from . import views 
app_name = "stroke"

urlpatterns = [
    path('', views.predict, name = 'stroke'), 
    path('predict/', views.predict_chances, name = 'submit_prediction'), 
    path('results/', views.view_results, name='results'),
]
