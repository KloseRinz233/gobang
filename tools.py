def check_position(array,x,y):
    if(x<0 or x>14 or y<0 or y>14):
        return False
    else:
        return array[x][y]
def check_surrounding(array,x,y,deep):
    for i in range(-deep,deep+1):
        for j in range(-deep,deep+1):
            if((i!=0 or j!=0) and (check_position(array,x+i,y+j)==1 or check_position(array,x+i,y+j)==2)):
                  return 1
    return 0    
def get_possible_position(array):
    possible_position1=[]
    possible_position2=[]
    for i in range(0,15):
        for j in range(0,15):
            if(check_surrounding(array,i,j,1) and check_position(array,i,j)==0):
                possible_position1.append([i,j])
            elif(check_surrounding(array,i,j,2) and check_position(array,i,j)==0):
                possible_position2.append([i,j])
    possible_position1.extend(possible_position2)
    return possible_position1   
def check_win(array):
    chess_type=0
    flag=1
    draw=1
    for i in range(0,15):
        for j in range(0,15):
            if(check_position(array,i,j)==1 or check_position(array,i,j)==2):
                chess_type=check_position(array,i,j)
                flag=1
                for k in range(1,5):
                    if(check_position(array,i-k,j)!=chess_type):
                        flag=0
                        break
                if(flag==1):
                   return [chess_type,'win']

                flag=1
                for k in range(1,5):
                    if(check_position(array,i-k,j-k)!=chess_type):
                        flag=0
                        break
                if(flag==1):
                   return [chess_type,'win']

                flag=1
                for k in range(1,5):
                    if(check_position(array,i,j-k)!=chess_type):
                        flag=0
                        break
                if(flag==1):
                   return [chess_type,'win']
                 
                flag=1
                for k in range(1,5):
                    if(check_position(array,i-k,j+k)!=chess_type):
                        flag=0
                        break
                if(flag==1):
                   return [chess_type,'win']
            else:
                draw=0
    if(draw==1):
        return [0,'draw']
    return False