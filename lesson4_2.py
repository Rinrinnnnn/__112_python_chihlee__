{
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
import pyinputplus as pyip

scores = pyip.inputInt("請輸入學生分數(最高300分):",min=0,max=300)
print(scores)
isYes = pyip.inputMenu(['y','n'],prompt="學生是否符合加分條件(請選擇1或2)?\n",numbered=True)
print()
print(isYes)