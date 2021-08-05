from django import forms
from django.forms import fields
from .models import LinearModel

class UygulamaFormu(forms.Form):
    Overal = forms.FloatField(label="Ortalama")
    Height = forms.FloatField(label="Boy")
    Weight = forms.FloatField(label="Kilo")
    Age = forms.FloatField(label="Yaş")
    WeakFoot = forms.FloatField(label="Zayıf Ayak Yeteneği")
    SkillMoves = forms.FloatField(label="Beceri Hareketleri")
    Value = forms.FloatField(label="Piyas Değeri")
    Wage = forms.FloatField(label="Haftalık Maaşı(€)")
    Positions = ( ('CAM' ,"CAM"),
            ('CB'  ,"CB"),
            ('CDM' ,"CDM"),
            ('CF'  ,"CF"),
            ('CF'  ,"CM"),
            ('GK'  ,"GK"),
            ('LB'  ,"LB"),
            ('LM'  ,"LM"),
            ('LW'  ,"LW"),
            ('LWB' ,"LWB"),
            ('RB'  ,"RB"),
            ('RM'  ,"RM"),
            ('RW'  ,"RW"),
            ('RWB' ,"RWB"),
            ('ST'  ,"ST") )
    Position = forms.ChoiceField(choices=Positions,label="Pozisyon")
    WorkRates = ( ('High/High' ,"High/High"),
            ('High/Low'  ,"High/Low"),
            ('High/Medium' ,"High/Medium"),
            ('Low/High'  ,"Low/High"),
            ('Low/Low'  ,"Low/Low"),
            ('Low/Medium'  ,"Low/Medium"),
            ('Medium/High'  ,"Medium/High"),
            ('Medium/Low'  ,"Medium/Low"),
            ('Medium/Medium'  ,"Medium/Medium"))
    WorkRate = forms.ChoiceField(choices=WorkRates,label="Çalışma Oranları")
    Foots = ( ('Right','Sağ'),
              ('Left','Sol'))
    PreferredFoot_R = forms.ChoiceField(choices=Foots,label="Tercih Ettiği Ayak",widget=forms.RadioSelect)
    GKSkills = forms.FloatField(label="Kalecilik Yetenekleri")
    Shooting = forms.FloatField(label="Şut Yetenekleri")
    Physical = forms.FloatField(label="Fiziki Yetenekleri")
    Mental = forms.FloatField(label="Mental Kabiliyeti")
    Defence = forms.FloatField(label="Defansif Yeteneği")
    Passing = forms.FloatField(label="Pas Yeteneği")
    BallSkills = forms.FloatField(label="Topla Oynama Becerisi")

class PredictForm(forms.ModelForm):
        class Meta:
                model = LinearModel
                fields = ["isim","Overal","Height","Weight","Age","WeakFoot","SkillMoves","Value","Wage","Position","WorkRate","PreferredFoot_R",
                "GKSkills","Shooting","Physical","Mental","Defence","Passing","BallSkills"]
