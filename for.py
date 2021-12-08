def temp (c):
    if c > 100:
        print('forró')
    elif c == 100:
        print('forr.pont')
    elif 60 < c < 100:
        print('forró')
    elif 40 < c < 80:
        print('nagyon meleg')
    elif 20 < c < 60:
        print('meleg')
    elif 0 < c < 40:
        print('normál')
    elif c == 0:
        print('fagy.pont')
    elif c < 0:
        print('fagyás')
for x in reversed(range(-20, 121, 20)):
    print (x, end="")
    print("c ---> " ,end="")
    temp (x)
