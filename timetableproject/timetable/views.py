from django.shortcuts import render
from .models import TimeSlot

DAY_ORDER = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
             'Thursday': 4, 'Friday': 5, 'Saturday': 6}

def timetable_view(request):
    slots = sorted(TimeSlot.objects.all(),
                   key=lambda s: (DAY_ORDER.get(s.day, 99), s.start_time))
    return render(request, 'timetable/timetable.html', {'slots': slots})
