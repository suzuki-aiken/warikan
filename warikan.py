"""
割り勘アプリ

きんがくと人数を受け取り
割り勘計算をうけとる

1500円　3人　1人あたり500円　あまりは　0円

500円　3人　1人あたり166円　あまりは　2円
"""
def warikan():
   # number_nin=int(input(number))
   # money_yen=int(input(money))

   #入力
   number_nin=int(input("number>"))
   money_yen=int(input("money>"))

   #計算
   money_wari=money_yen // number_nin
   money_amari= money_yen % number_nin

   #出力
   print("一人当たり"+str(money_wari)+"円　余りは"+str(money_amari)+"円")

def main_answer():
    #入力
    総支払額 = 1500
    amount = 500
    人数 =3 % number_of_people
    member = 3

    payment = amount // 人数

    amari = amount % 人数 %remainder

    #出力 f-string F記法
    print(f'一人あたりは{payment}円です。端数は{amari}円です。')

if __name__ == '__main__':
    main_answer()
    warikan()

