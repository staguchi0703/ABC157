# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
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
N, M, K = [int(item) for item in input().split()]
fri_list = [[int(item) for item in input().split()] for _ in range(M)]
bro_list = [[int(item) for item in input().split()] for _ in range(K)]

grid = np.zeros((N,N), dtype='int')

for i, j in fri_list:
    grid[i-1,j-1] = 1
    grid[j-1,i-1] = 1

for i, j in bro_list:
    grid[i-1,j-1] = 2
    grid[j-1,i-1] = 2

print(grid)