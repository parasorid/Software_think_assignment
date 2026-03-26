import datetime
now = datetime.datetime.now()

if now.hour<12:
    print("현재는 24시 표시 기준 {Hour}시로 오전입니다.".format(Hour=now.hour))
else:
    print("현재는 24시 표시 기준 {Hour}시로 오후입니다.".format(Hour=now.hour))