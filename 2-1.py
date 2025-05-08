# n個の整数が互いに全て異なるのかを確認
# 全て互いに異なる場合は"YES"、そうでない場合は"NO"と出力
# i番目の整数は、a(i)と表す
import sys

# 標準入力
n = int(input())
a = list(map(int, input().split()))

# 標準入力の代わり
#n: int = 5
#a = [3, 2, 5, 1, 1]

# 入力エラー処理
if(n < 1 or n > 50):
    print(f"Error：不適切な値が入力されました n={n}")
    sys.exit()
elif(n > len(a)):
    print("Error：入力した整数の数が不足しています")
    sys.exit()
elif(n < len(a)):
    print("Error：入力した整数の数が多すぎます")
    sys.exit()

for check in a:
    if(check < 1 or check > 1000):
        print(f"Error：不適切な値が入力されました a(i)={check}")
        sys.exit()

# main処理
# 入力list(a)の要素数と、重複を削除したset(a)の要素数が同一か判定
# 同一：False
# 同一でない：True
flag = len(a) != len(set(a))

if(flag == True):
    print("NO")
else:
    print("YES")
