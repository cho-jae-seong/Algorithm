import sys
from copy import deepcopy

def dfs(idx,maps):
    global min_result
    if idx==len(cctv_location):
        value=0
        for i in range(len(maps)):
            value+=maps[i].count('0')
        min_result=min(min_result,value)
        return

    for i in range(len(cctv_direction[idx])):
        next_maps=deepcopy(maps)
        x,y=cctv_location[idx]
        survelliance(next_maps,x,y,cctv_direction[idx][i])
        dfs(idx+1,next_maps)
    return

def survelliance(maps,x,y,direcs):
    for direc in direcs:
        nx,ny=x,y
        if direc=='u':
            k=0
        elif direc=='d':
            k=1
        elif direc=='l':
            k=2
        elif direc=='r':
            k=3
        while True:
            nx+=dx[k]
            ny+=dy[k]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]=='6':
                    break
                elif maps[nx][ny]=='0':
                    maps[nx][ny]='#'
            else:
                break
    return

def find_cctv():
    cctv_location=[]
    cctv_direction=[]
    for i in range(n):
        for j in range(m):
            if cctv[i][j]=='1':
                cctv_location.append((i,j))
                cctv_direction.append(['u','d','l','r'])
            elif cctv[i][j]=='2':
                cctv_location.append((i,j))
                cctv_direction.append(['ud','lr'])
            elif cctv[i][j]=='3':
                cctv_location.append((i,j))
                cctv_direction.append(['ul','rd','dl','lu'])
            elif cctv[i][j]=='4':
                cctv_location.append((i,j))
                cctv_direction.append(['lur','urd','rdl','dlu'])
            elif cctv[i][j]=='5':
                k=0
                cx,cy=i,j
                while k<4:
                    nx=cx+dx[k]
                    ny=cy+dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if cctv[nx][ny]=='6':
                            cx,cy=i,j
                            k+=1
                        elif cctv[nx][ny]=='0':
                            cctv[nx][ny]='#'
                            cx,cy=nx,ny
                        else:
                            cx,cy=nx,ny
                    else:
                        cx,cy=i,j
                        k+=1
    return cctv_location,cctv_direction


n,m=map(int, sys.stdin.readline().split())
cctv=[sys.stdin.readline().split() for i in range(n)]
min_result=64
dx,dy=[-1,1,0,0],[0,0,-1,1]
cctv_location,cctv_direction=find_cctv()
dfs(0,cctv)
print(min_result)


        