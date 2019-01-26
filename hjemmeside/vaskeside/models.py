from django.db import models
from django.contrib.auth.models import User


timetable = []
lsttimetable = []

for i in range(8, 22):
    temp = []
    time = str(i) + ':00'
    lsttimetable.append(time)
    timetable.append(tuple([time, time]))


# konverterer fra f.eks [8:00, 10:00] til [8:00, 9:00, 10:00]
def converttime(pendingtime):
    temp = False
    takentime = []
    for time in lsttimetable:
        if time == pendingtime[0]:
            takentime.append(time)
            temp = True
            continue
        elif time == pendingtime[1]:
            takentime.append(time)
            break
        elif temp:
            takentime.append(time)
    return takentime


# konverterer fra [8:00, 10:00] til [8:00-9:00, 9:00-10:00]
def converttimespace(pendingtime):
    pendingtime = converttime(pendingtime)
    space = []
    for integer in range(len(pendingtime)):
        try:
            space.append(pendingtime[integer] + '-' + pendingtime[integer + 1])
        except Exception:
            break
    return space


def notavtime(pendingtime, maskine):
    starttid, sluttid = pendingtime[0].split(':')[0], pendingtime[len(pendingtime) - 1].split(':')[0]
    if int(starttid) >= int(sluttid):
        return False, None
    pendingspace = converttimespace(pendingtime)
    notav = Tables.objects.filter(maskine=maskine)
    takens = [[i.starttid, i.sluttid] for i in notav]
    takenspace = list(map(lambda lst: converttimespace(lst), takens))
    for i in pendingspace:
        for j in takenspace:
            if i in j:
                return False, None

    if len(pendingspace) > 3:
        return False, None

    return True, len(pendingspace) * 60


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
