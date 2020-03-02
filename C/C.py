# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
N, M = [int(item) for item in input().split()]

reg_list = [[int(item) for item in input().split()] for _ in range(M)]

cand = [11 for _ in range(N)]

is_flag = False

for i, v in reg_list:
    temp = cand[i-1]
    cand[i-1] = min(v, temp)
    if temp < 11 and v != temp:
        is_flag = True
    if i == 1 and v == 0:
        is_flag = True

# print(cand)

res = ''
for j, v in enumerate(cand):
    if v == 11 and j > 0:
        res += '0'
    elif v ==11 and j == 0:
        res += '1'
    else:
        res += str(v)

if is_flag and N >1:
    print(-1)
elif N == 1 and M > 1:
    print(-1)
elif N == 1 and M ==1:
    print(res)
elif N ==1 and M == 0:
    print(0)
else:
    print(res)
    