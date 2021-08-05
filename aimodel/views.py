from .models import LinearModel
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from .forms import UygulamaFormu,PredictForm
from django.contrib.auth.decorators import login_required
import joblib
# Create your views here.
@login_required(login_url="user:login")
def predicts(request):
    keyword = request.GET.get("keyword")

    if keyword:
        predicts = LinearModel.objects.filter(isim__contains = keyword)
        return render(request,"predicts.html",{"predicts":predicts})

    predicts = LinearModel.objects.all()
    return render(request,"predicts.html",{"predicts":predicts})
    
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"anasayfa.html")

@login_required(login_url="user:login")
def dashboard(request):
    predicts = LinearModel.objects.filter(user = request.user)
    context = {"predicts":predicts}
    return render(request,"dashboard.html",context)

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def newpredict(request):
    form = PredictForm(request.POST or None)
    if form.is_valid():
        linearml = joblib.load("model_joblib")
        predict = form.save(commit=False)
        position_dict = {"CAM":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         "CB":[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         "CDM":[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                         "CF":[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                         "CM":[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                         "GK":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
                         "LB":[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                         "LM":[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                         "LW":[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                         "LWB":[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                         "RB":[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                         "RM":[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
                         "RW":[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                         "RWB":[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                         "ST":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]}
        workrate_dict = {'High/High':[1,0,0,0,0,0,0,0,0],
            'High/Low'  :[0,1,0,0,0,0,0,0,0],
            'High/Medium' :[0,0,1,0,0,0,0,0,0],
            'Low/High'  :[0,0,0,1,0,0,0,0,0],
            'Low/Low'  :[0,0,0,0,1,0,0,0,0],
            'Low/Medium' :[0,0,0,0,0,1,0,0,0],
            'Medium/High'  :[0,0,0,0,0,0,1,0,0],
            'Medium/Low'  :[0,0,0,0,0,0,0,1,0],
            'Medium/Medium'  :[0,0,0,0,0,0,0,0,1]}
        foot_dict = {'Sağ':1.0,'Sol':0.0}
        foot_get = form.cleaned_data.get("PreferredFoot_R")
        position_get = form.cleaned_data.get("Position")
        workrate_get = form.cleaned_data.get("WorkRate")
        ml_position = position_dict.get(position_get)
        ml_workrate = workrate_dict.get(workrate_get)
        ml_foot = foot_dict.get(foot_get)
        overal = form.cleaned_data.get("Overal")
        height = form.cleaned_data.get("Height")
        weight = form.cleaned_data.get("Weight")
        age = form.cleaned_data.get("Age")
        weakfoot = form.cleaned_data.get("WeakFoot")
        skill = form.cleaned_data.get("SkillMoves")
        value = form.cleaned_data.get("Value")
        wage = form.cleaned_data.get("Wage")
        gk = form.cleaned_data.get("GKSkills")
        shoot = form.cleaned_data.get("Shooting")
        physical = form.cleaned_data.get("Physical")
        mental = form.cleaned_data.get("Mental")
        defence = form.cleaned_data.get("Defence")
        passing = form.cleaned_data.get("Passing")
        ballskills = form.cleaned_data.get("BallSkills")
        ml_result=linearml.predict([[overal,height,weight,age,weakfoot,skill,value,wage,
        ml_position[0],ml_position[1],ml_position[2],ml_position[3],ml_position[4],ml_position[5],ml_position[6],ml_position[7],
        ml_position[8],ml_position[9],ml_position[10],ml_position[11],ml_position[12],ml_position[13],ml_position[14],
        ml_workrate[0],ml_workrate[1],ml_workrate[2],ml_workrate[3],ml_workrate[4],ml_workrate[5],ml_workrate[6],ml_workrate[7],ml_workrate[8],
        ml_foot,gk,shoot,physical,mental,defence,passing,ballskills]])

        predict.user = request.user
        predict.Result = ml_result
        predict.save()

        messages.success(request,"Tahmin başarıyla gerçekleştirildi.")
        return redirect("index")

    return render(request,"newpredict.html",{"form":form})

def detail(request,id):
    #predict = LinearModel.objects.filter(id = id).first()
    predict = get_object_or_404(LinearModel,id=id)   
    return render(request,"detail.html",{"predict":predict})

@login_required(login_url="user:login")
def updatePredict(request,id):
    predict = get_object_or_404(LinearModel,id=id)
    form = PredictForm(request.POST or None,instance=predict)
    if form.is_valid():
        linearml = joblib.load("model_joblib")
        predict = form.save(commit=False)
        position_dict = {"CAM":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         "CB":[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         "CDM":[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                         "CF":[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                         "CM":[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                         "GK":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
                         "LB":[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                         "LM":[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                         "LW":[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                         "LWB":[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                         "RB":[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                         "RM":[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
                         "RW":[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                         "RWB":[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                         "ST":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]}
        workrate_dict = {'High/High':[1,0,0,0,0,0,0,0,0],
            'High/Low'  :[0,1,0,0,0,0,0,0,0],
            'High/Medium' :[0,0,1,0,0,0,0,0,0],
            'Low/High'  :[0,0,0,1,0,0,0,0,0],
            'Low/Low'  :[0,0,0,0,1,0,0,0,0],
            'Low/Medium' :[0,0,0,0,0,1,0,0,0],
            'Medium/High'  :[0,0,0,0,0,0,1,0,0],
            'Medium/Low'  :[0,0,0,0,0,0,0,1,0],
            'Medium/Medium'  :[0,0,0,0,0,0,0,0,1]}
        foot_dict = {'Sağ':1.0,'Sol':0.0}
        foot_get = form.cleaned_data.get("PreferredFoot_R")
        position_get = form.cleaned_data.get("Position")
        workrate_get = form.cleaned_data.get("WorkRate")
        ml_position = position_dict.get(position_get)
        ml_workrate = workrate_dict.get(workrate_get)
        ml_foot = foot_dict.get(foot_get)
        overal = form.cleaned_data.get("Overal")
        height = form.cleaned_data.get("Height")
        weight = form.cleaned_data.get("Weight")
        age = form.cleaned_data.get("Age")
        weakfoot = form.cleaned_data.get("WeakFoot")
        skill = form.cleaned_data.get("SkillMoves")
        value = form.cleaned_data.get("Value")
        wage = form.cleaned_data.get("Wage")
        gk = form.cleaned_data.get("GKSkills")
        shoot = form.cleaned_data.get("Shooting")
        physical = form.cleaned_data.get("Physical")
        mental = form.cleaned_data.get("Mental")
        defence = form.cleaned_data.get("Defence")
        passing = form.cleaned_data.get("Passing")
        ballskills = form.cleaned_data.get("BallSkills")
        ml_result=linearml.predict([[overal,height,weight,age,weakfoot,skill,value,wage,
        ml_position[0],ml_position[1],ml_position[2],ml_position[3],ml_position[4],ml_position[5],ml_position[6],ml_position[7],
        ml_position[8],ml_position[9],ml_position[10],ml_position[11],ml_position[12],ml_position[13],ml_position[14],
        ml_workrate[0],ml_workrate[1],ml_workrate[2],ml_workrate[3],ml_workrate[4],ml_workrate[5],ml_workrate[6],ml_workrate[7],ml_workrate[8],
        ml_foot,gk,shoot,physical,mental,defence,passing,ballskills]])

        predict.user = request.user
        predict.Result = ml_result
        predict.save()

        messages.success(request,"Tahmin başarıyla güncellendi.")
        return redirect("aimodel:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deletePredict(request,id):
    predict = get_object_or_404(LinearModel,id=id)
    predict.delete()

    messages.warning(request,"Tahmin başarıyla silindi!")
    return redirect("aimodel:dashboard")
