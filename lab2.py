height, weight, kol_vo, time = map(float, input().split())
step = height/4 + 0.37
dist = step*kol_vo
print('Пройденная дистанция', dist)
speed = dist/time
energy = 0.035 * weight + (speed*speed/height)*0.029*weight
print('Калории', energy)
