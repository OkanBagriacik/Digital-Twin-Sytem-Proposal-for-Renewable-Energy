from django.db import models


class Energy(models.Model):
    country = models.CharField('country', max_length=200)
    year = models.IntegerField('year', default=0)
    month = models.CharField('month', max_length=200)
    day = models.IntegerField('day', default=0)
    SolarPV_Consumption = models.IntegerField('SolarPV_Consumption', default=0)
    Panel_Count = models.IntegerField('Panel_Count', default=0)
    BelowUnderAVG = models.IntegerField('BelowUnderAVG', default=0)
    Weather = models.IntegerField('Weather', default=0)

    def __str__(self):
        return 'Data of ' + str(self.day) + " " + str(self.month) + " " + str(self.year)
