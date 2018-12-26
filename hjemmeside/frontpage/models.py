from django.db import models
from django.contrib.auth.models import User


timetable = []
lsttimetable = []

for i in range(8, 22):
    temp = []
    time = str(i) + ':00'
    lsttimetable.append(time)
    temp.append(time)
    temp.append(time)
    timetable.append(tuple(temp))


def converttime(rmtimes):
    temp = False
    takentime = []
    for time in lsttimetable:
        if time == rmtimes[0]:
            takentime.append(time)
            temp = True
            continue
        elif time == rmtimes[1]:
            takentime.append(time)
            break
        elif temp:
            takentime.append(time)
    return takentime


def converttimespace(takentime):
    space = []
    for integer in range(len(takentime)):
        try:
            space.append(takentime[integer] + '-' + takentime[integer+1])
        except Exception:
            break
    return space


def notavtime(rmtimes, maskine):
    starttid, sluttid = rmtimes[0].split(':')[0], rmtimes[len(rmtimes)-1].split(':')[0]
    if int(starttid) >= int(sluttid):
        return False, ''
    takentime = converttime(rmtimes)
    notav = Taken.objects.filter(maskine=maskine)
    colunmlen = (len(takentime) - 1) * 60
    takentime = converttimespace(takentime)
    for f in takentime:
        for i in notav:
            if i.time == f:
                return False, None

    if len(takentime) > 3:
        return False, None
    for i in takentime:
        Taken(time=i, maskine=maskine).save()
    return True, colunmlen


maskiner = (('Sønderhus vask 3', 'Sønderhus vask 3'),
            ('Sønderhus vask 2', 'Sønderhus vask 2'),
            ('Sønderhus vask 1', 'Sønderhus vask 1'),
            ('Damgårdens vask', 'Damgårdens vask'))


class Tables(models.Model):
    maskine = models.CharField(max_length=255, choices=maskiner, default='Sønderhus Vask 1')
    starttid = models.CharField(max_length=255, choices=timetable, default='8:00')
    sluttid = models.CharField(max_length=255, choices=timetable, default='10:00')
    columnlen = models.IntegerField()
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)

    def __str__(self):
            return self.maskine


class Taken(models.Model):
    time = models.CharField(max_length=255)
    maskine = models.CharField(max_length=255, choices=maskiner, default='Sønderhus vask 1')

    def __str__(self):
        return self.time


