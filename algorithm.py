import random
import tools
from eva import evaluation

EMPTY=0
BLACK=1
WHITE=2  
MIN=-10000000
MAX=10000000 

def choose(chesspad,deep,player):
    points=tools.get_possible_position(chesspad)    #读取可下棋位置
    best=MIN                #初始化评分
    bestpoint=[]            #初始化最优下棋位置
    global p1,p2
    p1=player
    if player==1:
        p2=2
    else:
        p2=1
    alpha=10000000
    beta=-10000000

    for i in range(len(points)):
        chesspad[points[i][0]][points[i][1]]=p1
        score=Min(chesspad,deep-1,alpha,best if best>beta else beta)

        if score==best:
            bestpoint.append(points[i])
        if score>best:
            best=score
            bestpoint=[]
            bestpoint.append(points[i])
        chesspad[points[i][0]][points[i][1]]=0
    result=random.choice(bestpoint)
    return result               

def Min(chesspad,deep,alpha,beta):
    score=evaluation().evaluate(chesspad,p1)
    if(deep<=0 or (tools.check_win(chesspad)!=False)):          #Win为获胜棋盘得分
        return score
    
    points=tools.get_possible_position(chesspad)    #读取可下棋位置
    best=MAX                #初始化评分
    
    for i in range(len(points)):
        chesspad[points[i][0]][points[i][1]]=p2
        score=Max(chesspad,deep-1,best if best<alpha else alpha,beta)
        chesspad[points[i][0]][points[i][1]]=0
        if score<best:
            best=score
        if score<beta:
            break
    return best

def Max(chesspad,deep,alpha,beta):
    score=evaluation().evaluate(chesspad,p1)
    if(deep<=0 or (tools.check_win(chesspad)!=False)):          #Win为获胜棋盘得分
        return score
    
    points=tools.get_possible_position(chesspad)    #读取可下棋位置
    best=MIN                #初始化评分
    
    for i in range(len(points)):
        chesspad[points[i][0]][points[i][1]]=p1
        score=Min(chesspad,deep-1,alpha,best if best>beta else beta)
        chesspad[points[i][0]][points[i][1]]=0
        if score>best:
            best=score
        if score>alpha:
            break
    return best
#chesspad=[]
#f=open("chesspad.txt","r")
#for line in f:
#    chesspad.append(list(map(int,line.split())))
#f.close()
#print(chosse(chesspad,1,2))
