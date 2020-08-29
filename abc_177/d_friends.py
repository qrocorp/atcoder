x = list(map(int, input().split()))
n = x[0]
m = x[1]

xy = []
for i in range(m):
    xy.append(list(map(int, input().split())))

# 友だちでグループを作る

start_group = list(range(1, n+1))
friend_groups = []

for i in range(m):
    if xy[i][0]:
