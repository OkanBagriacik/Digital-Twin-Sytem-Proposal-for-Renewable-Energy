import django_filters

from .models import *
from distutils.util import strtobool

EMPTY_CHOICE = ('', 'Please Select Country'),
EMPTY_CHOICE1 = ('', 'Please Select Year'),
EMPTY_CHOICE2 = ('', 'Please Select Month'),
EMPTY_CHOICE3 = ('', 'Please Select Day'),
EMPTY_CHOICE4 = ('', 'Please Select Solar Pv'),
EMPTY_CHOICE5 = ('', 'Please Select Panel Count'),
EMPTY_CHOICE6 = ('', 'Please Select Average'),
EMPTY_CHOICE7 = ('', 'Please Select Weather'),


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Energy
        fields = ['country', 'year', 'month', 'day', 'SolarPV_Consumption', 'Panel_Count', 'BelowUnderAVG', 'Weather']
        exclude = ['id']
        widgets = {
            'country': django_filters.TypedChoiceFilter(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
        }

    def __init__(self, *args):
        super().__init__()
        self.filters['country'].extra['choices'] = EMPTY_CHOICE + args[1] + self.filters['country'].extra['choices']
        self.filters['year'].extra['choices'] = EMPTY_CHOICE1 + args[2] + self.filters['year'].extra['choices']
        self.filters['month'].extra['choices'] = EMPTY_CHOICE2 + args[3] + self.filters['month'].extra['choices']
        self.filters['day'].extra['choices'] = EMPTY_CHOICE3 + args[4] + self.filters['day'].extra['choices']
        self.filters['SolarPV_Consumption'].extra['choices'] = EMPTY_CHOICE4 + args[5] + \
                                                               self.filters['SolarPV_Consumption'].extra[
                                                                   'choices']
        self.filters['Panel_Count'].extra['choices'] = EMPTY_CHOICE5 + args[6] + self.filters['Panel_Count'].extra[
            'choices']
        self.filters['BelowUnderAVG'].extra['choices'] = EMPTY_CHOICE6 + args[7] + self.filters['BelowUnderAVG'].extra[
            'choices']
        self.filters['Weather'].extra['choices'] = EMPTY_CHOICE7 + args[8] + self.filters['Weather'].extra['choices']

    country = django_filters.TypedChoiceFilter(choices=(()), coerce=strtobool)
    year = django_filters.TypedChoiceFilter(choices=(()), coerce=strtobool)
    day = django_filters.TypedChoiceFilter(choices=(()), coerce=strtobool)
    month = django_filters.TypedChoiceFilter(choices=(()), coerce=strtobool)
    SolarPV_Consumption = django_filters.TypedChoiceFilter(choices=(()), coerce=strtobool)
    Panel_Count = django_filters.TypedChoiceFilter(choices=(()), coerce=strtobool)
    BelowUnderAVG = django_filters.TypedChoiceFilter(choices=(()), coerce=strtobool)
    Weather = django_filters.TypedChoiceFilter(choices=(()), coerce=strtobool)


class OrderFilterFromData(django_filters.FilterSet):
    class Meta:
        model = Energy
        fields = ['country', 'year', 'month', 'day', 'SolarPV_Consumption', 'Panel_Count', 'BelowUnderAVG', 'Weather']
        exclude = ['id']
