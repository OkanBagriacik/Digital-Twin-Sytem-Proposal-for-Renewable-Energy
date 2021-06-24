from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, FileResponse, Http404
from .filter import *

from polls.models import Energy


def index(request):
    template = loader.get_template('polls/index.html')

    return HttpResponse(template.render({"control": "index"}, request))


def report(request):
    template = loader.get_template('polls/index.html')
    context = {"deneme": 2}
    return HttpResponse(template.render({"control": "report"}, request))


def presentation(request):
    template = loader.get_template('polls/index.html')
    context = {"deneme": 2}
    return HttpResponse(template.render(context, request))


def graphs(request):
    template = loader.get_template('polls/index.html')
    context = {"deneme": 2}
    return HttpResponse(template.render(context, request))


def declaration(request):
    template = loader.get_template('polls/index.html')
    context = {"deneme": 2}
    return HttpResponse(template.render(context, request))

def dataRep(request):
    template = loader.get_template('polls/index.html')
    context = Energy.objects.all()[0:]
    monthLabels = Energy.objects.all().values_list('month', flat=True).distinct()
    yearLabel = Energy.objects.all().values_list('year', flat=True).distinct()
    return HttpResponse(
        template.render({"control": "dataReps", "context": list(context), "monthLabels": list(monthLabels),
                         "yearLabel": list(yearLabel)},
                        request))


def speResults(request):
    template = loader.get_template('polls/index.html')
    data = Energy.objects.all()

    countryLabels = data.values_list('country', flat=True).distinct()
    countrydict = {}

    for i in range(len(countryLabels)):
        countrydict[countryLabels[i]] = countryLabels[i]
    list = [(k, v) for k, v in countrydict.items()]

    yearLabels = data.values_list('year', flat=True).distinct()
    yearDict = {}
    for i in range(len(yearLabels)):
        yearDict[yearLabels[i]] = yearLabels[i]
    list1 = [(k, v) for k, v in yearDict.items()]

    monthLabels = data.values_list('month', flat=True).distinct()
    monthDict = {}
    for i in range(len(monthLabels)):
        monthDict[monthLabels[i]] = monthLabels[i]
    list2 = [(k, v) for k, v in monthDict.items()]

    dayLabels = data.values_list('day', flat=True).distinct()
    dayDict = {}
    for i in range(len(dayLabels)):
        dayDict[dayLabels[i]] = dayLabels[i]
    list3 = [(k, v) for k, v in dayDict.items()]

    SolarLabels = data.values_list('SolarPV_Consumption', flat=True).distinct()
    SolarDict = {}
    for i in range(len(SolarLabels)):
        SolarDict[SolarLabels[i]] = SolarLabels[i]
    list4 = [(k, v) for k, v in SolarDict.items()]

    PanelLabels = data.values_list('Panel_Count', flat=True).distinct()
    PanelDict = {}
    for i in range(len(PanelLabels)):
        PanelDict[PanelLabels[i]] = PanelLabels[i]
    list5 = [(k, v) for k, v in PanelDict.items()]

    AvgLabels = data.values_list('BelowUnderAVG', flat=True).distinct()
    AvgDict = {}
    for i in range(len(AvgLabels)):
        AvgDict[AvgLabels[i]] = "Under Avg" if AvgLabels[i] == 1 else "Not under Avg"
    list6 = [(k, v) for k, v in AvgDict.items()]

    WeatherLabels = data.values_list('Weather', flat=True).distinct()
    WeatherDict = {}
    for i in range(len(WeatherLabels)):
        WeatherDict[WeatherLabels[i]] = "Sunny" if WeatherLabels[i] == 1 else "Not Sunny"
    list7 = [(k, v) for k, v in WeatherDict.items()]

    my_filter = OrderFilter(request.GET, tuple(list), tuple(list1), tuple(list2), tuple(list3), tuple(list4),
                            tuple(list5), tuple(list6), tuple(list7))
    my_filter2 = OrderFilterFromData(request.GET)
    print(my_filter2.qs)
    context = {"control": "datafilter", "filter": my_filter, "filteredData": my_filter2.qs}

    return HttpResponse(template.render(context, request))
