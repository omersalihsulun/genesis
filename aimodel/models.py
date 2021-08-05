from django.db import models
# Create your models here.

class LinearModel(models.Model):
    user = models.ForeignKey("auth.user",on_delete= models.CASCADE)
    isim = models.CharField(max_length=50)
    Overal = models.FloatField(verbose_name="Ortalama",default=70)
    Height = models.FloatField(verbose_name="Boy",default= 175)
    Weight = models.FloatField(verbose_name="Kilo",default=70)
    Age = models.FloatField(verbose_name="Yaş",default=18)
    WeakFoot = models.FloatField(verbose_name="Zayıf Ayak Yeteneği",default=3)
    SkillMoves = models.FloatField(verbose_name="Beceri Hareketleri",default=3)
    Value = models.FloatField(verbose_name="Piyas Değeri",default=15000000)
    Wage = models.FloatField(verbose_name="Haftalık Maaşı(€)",default=50000)
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
    Position = models.CharField(max_length=50,choices=Positions,verbose_name="Mevkisi",default="CAM")
    WorkRates = ( ('High/High' ,"High/High"),
            ('High/Low'  ,"High/Low"),
            ('High/Medium' ,"High/Medium"),
            ('Low/High'  ,"Low/High"),
            ('Low/Low'  ,"Low/Low"),
            ('Low_Medium'  ,"Low_Medium"),
            ('Medium/High'  ,"Medium/High"),
            ('Medium/Low'  ,"Medium/Low"),
            ('Medium/Medium'  ,"Medium/Medium"))
    WorkRate = models.CharField(max_length=50,choices=WorkRates,verbose_name="Çalışma Oranları",default="Medium/Medium")
    Foots = ( ('Sağ','Sağ'),
              ('Sol','Sol'))
    PreferredFoot_R = models.CharField(max_length=50,choices=Foots,verbose_name="Tercih Ettiği Ayak",default="Sağ")
    GKSkills = models.FloatField(verbose_name="Kalecilik Yetenekleri",default=70)
    Shooting = models.FloatField(verbose_name="Şut Yetenekleri",default=70)
    Physical = models.FloatField(verbose_name="Fiziki Yetenekleri",default=70)
    Mental = models.FloatField(verbose_name="Mental Kabiliyeti",default=70)
    Defence = models.FloatField(verbose_name="Defansif Yeteneği",default=70)
    Passing = models.FloatField(verbose_name="Pas Yeteneği",default=70)
    BallSkills = models.FloatField(verbose_name="Topla Oynama Becerisi",default=70)
    Result = models.FloatField(verbose_name="Tahmini Potansiyeli",default=70)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.isim