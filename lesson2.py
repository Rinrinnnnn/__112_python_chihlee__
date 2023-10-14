side=int(input('請輸入對邊：'))
another_side=int(input('請輸入斜邊:'))

import math #import導入其他模組用
radian=math.asin(side/another_side) #計算出弧度(小數點)
degree=math.degrees(radian) #弧度換算角度
print(round(degree,ndigits=2)) #類似四捨五入