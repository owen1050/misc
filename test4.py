arr = [12,31,63,95,99,154,198,221,304,346,411,455,537]
ser = [40,32,55,48,18,50 ,48 ,18 ,28 ,54 ,40 ,72 ,12 ]

t = 0
done = False
arrI = 0
serI = 0

while arrI < len(arr):
    if t >= arr[arrI]:
        print(arr[arrI], t)
        t = t + ser[arrI]
        arrI = arrI + 1
    else:
        t = t + 1


print(t)
