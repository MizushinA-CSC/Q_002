# 以下の規則を守り、入力された楽譜S通りにピアノを演奏する秒数を出力
# (1) ピアノの鍵盤1つよりも小さなウサギが、1鍵盤ずつ移動して演奏する
# (2) ピアノに黒鍵はなく、白鍵盤のみ
# (3) ピアノは循環しておらず、ド(d)〜シ(c)の7鍵
# (4) ウサギが、鍵盤を1つ移動する/今乗っている鍵盤を弾く のにそれぞれ1秒かかる
# (5) うさぎは現在、ミ(m)の鍵盤に乗っている
import sys

# 標準入力
S = list(input())

# 標準入力の代わり
#S = list("mmmdcdc")

# 入力エラー処理
if(len(S) < 1 or len(S) > 100):
    print(f"Error：文字数が不適切です 入力文字数={len(S)}")
    sys.exit()

for check in S:
    if(check != "d" and check != "r" and check != "m" and check != "f" and check != "s" and check != "l" and check != "c"):
        print(f"Error：文字はd, r, m, f, s, l, cから入力してください ({check} is NG)")
        sys.exit()

# main処理
piano = ["d", "r", "m", "f", "s", "l", "c"]
rabit = "m"
time: int = 0

for i in S:
    if(i == rabit):
        time += 1
    else:
        time += abs(piano.index(i) - piano.index(rabit))   # 移動
        rabit = i
        time += 1   # 鍵盤を弾く

print(time)
