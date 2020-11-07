import datetime
def solution(a, b):
    weeks=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    d=datetime.date(2016,a,b)
    return weeks[d.weekday()]
