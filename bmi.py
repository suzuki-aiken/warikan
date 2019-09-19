"""
身長　cm
体重　kg

を受け取り　BMIを　小数第2位で出力
"""


def bmi(height,weight):
    number=weight/(height/100)**2
    return number

def bmi_answer()
    #入力 180cm 76kg -> 23.46 答えを書いておく
    height_cm = int(input(('身長は')))
    weight_kg = int(input(('体重は')))
    height_m = height_cm/100

    #計算
    height_m = height_cm/100

    #変数のインライン化
    bmi_rounded = round(weight_kg / (height_m ** 2), 2)
    print(bmi_rounded)

if __name__ == '__main__':
    height = float(input("身長："))
    weight = float(input("体重："))

    print (round(bmi(height,weight)),2)
