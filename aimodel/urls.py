from django.contrib import admin
from django.urls import path
from .import views

app_name="aimodel"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('newpredict/',views.newpredict,name="newpredict"),
    path('predict/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updatePredict,name="update"),
    path('delete/<int:id>',views.deletePredict,name="delete"),
    path('',views.predicts,name="predicts"),


]