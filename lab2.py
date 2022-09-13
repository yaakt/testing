height, weight, kol_vo, time = map(float, input().split())
step = height/4 + 0.37
dist = step*kol_vo/100
print('Пройденная дистанция', dist)
if dist < 2:
    print('Вы прошли короткую дистанцию')
elif dist < 4:
    print('Вы прошли среднюю дистанцию')
else:
    print('Вы прошли длинную дистанцию')
    
speed = dist/time
energy = 0.035 * weight + (speed*speed/height)*0.029*weight
print('Калории', energy)
