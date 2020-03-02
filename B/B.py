# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\B\B_input.txt', 'r', encoding="utf-8")
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
import numpy as np
first = [int(item) for item in input().split()]
second = [int(item) for item in input().split()]
third = [int(item) for item in input().split()]

grid = np.array([first, second, third])
# print(grid)

N = int(input())

num_list = [int(input()) for _ in range(N)]
# print(num_list)

flg_list = [0,0,0]

is_bingo = False

for i in range(3):
    flg_list = [0,0,0]
    for j in range(3):
        if grid[i,j] in num_list:
            flg_list[j] = 1

    if flg_list == [1,1,1]:
        is_bingo = True

for i in range(3):
    flg_list = [0,0,0]
    for j in range(3):
        if grid[j,i] in num_list:
            flg_list[j] = 1

    if flg_list == [1,1,1]:
        is_bingo = True


flg_list = [0,0,0]
for i in range(3):
    if grid[i,i] in num_list:
        flg_list[i] = 1

    if flg_list == [1,1,1]:
        is_bingo = True

flg_list = [0,0,0]
for i in range(3):

    if grid[2-i,i] in num_list:
        flg_list[i] = 1

    if flg_list == [1,1,1]:
        is_bingo = True

if is_bingo:
    print('Yes')
else:
    print('No')



