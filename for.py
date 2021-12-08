def temp (c):
    if c > 100:
        print('fnagyon orró')
    elif c == 100:
        print('forr.pont')
    elif 80 < c < 100:
        print('forró')
    elif 60 < c < 81:
        print('nagyon meleg')
    elif 40 < c < 61:
        print('meleg')
    elif 0 < c < 41:
        print('normál')
    elif c == 0:
        print('fagy.pont')
    elif c < 0:
        print('fagyás')
for x in reversed(range(-20, 121, 20)):
    print (x, end="")
    print("c ---> " ,end="")
    temp (x)







aktual_hom = int(input("Most hány fok van? "))
temp (aktual_hom)