from asyncio.windows_events import NULL
import tkinter

#紀錄正確道路
top=0
True_Path_x=[NULL]*200
True_Path_y=[NULL]*200

#紀錄所有走過的道路
topp=0
All_Path_x=[NULL]*200
All_Path_y=[NULL]*200

x=1
y=1
mx=1
my=1
te=0
checkreturn=[]
#迷宮
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]


while(1):
    maze[y][x]=2
    #終點位置
    if(x==13 and y==13): 
        True_Path_x[top]=13
        True_Path_y[top]=13
        #maze[13][13]=4
        All_Path_x[topp]=13
        All_Path_y[topp]=13
        break
    #偵測右邊有路
    if(maze[y][x+1]==0):
        maze[y][x]=2
        True_Path_x[top]=x
        True_Path_y[top]=y
        All_Path_x[topp]=x
        All_Path_y[topp]=y
        topp=topp+1
        x=x+1
        top=top+1
    #偵測上邊有路
    elif(maze[y-1][x]==0):
        maze[y][x]=2
        True_Path_x[top]=x
        True_Path_y[top]=y
        All_Path_x[topp]=x
        All_Path_y[topp]=y
        topp=topp+1
        y=y-1
        top=top+1
    #偵測左邊有路
    elif(maze[y][x-1]==0):
        maze[y][x]=2
        True_Path_x[top]=x
        True_Path_y[top]=y
        All_Path_x[topp]=x
        All_Path_y[topp]=y
        topp=topp+1
        x=x-1
        top=top+1
    #偵測下邊有路
    elif(maze[y+1][x]==0):
        maze[y][x]=2
        True_Path_x[top]=x
        True_Path_y[top]=y
        All_Path_x[topp]=x
        All_Path_y[topp]=y
        topp=topp+1
        y=y+1
        top=top+1
    #上述都未執行代表無路可走，True_Path會用返回上一個地點再偵測一次是否有路，沒有繼續返回上一個地點，直到TOP=-1 <--回到原仍然無路可走即沒有到終點的路
    else:
        All_Path_x[topp]=x
        All_Path_y[topp]=y
        topp=topp+1
        checkreturn.append(topp)
        top=top-1
        if (top<0):
            print("沒有出口")
            break
        x=True_Path_x[top]
        y=True_Path_y[top]
        
        
#走路
def main_proc():
    global te,mx,my
    mx=All_Path_x[te]
    my=All_Path_y[te]
    te=te+1
    if te in checkreturn:
        canvas.create_rectangle(mx*40,my*40,mx*40+39,my*40+39,fill="green",width=0)
    else:
        canvas.create_rectangle(mx*40,my*40,mx*40+39,my*40+39,fill="pink",width=0)    
    canvas.delete("MYCHR")
    canvas.create_image(mx*40+20,my*40+20,image=img,tag="MYCHR")
    
    #偵測是否到終點
    if(mx==True_Path_x[top] and my==True_Path_y[top]):
        label["text"]="恭喜過關"
    else:
        root.after(100,main_proc)
          
root=tkinter.Tk()
root.title("塗滿迷宮地板")

canvas=tkinter.Canvas(width=600,height=700,bg="white")
canvas.pack()
img=tkinter.PhotoImage(file="rat0.png")
canvas.create_image(mx*40+20,my*40+20,image=img,tag="MYCHR")

#製造牆壁
for y in range(15):
    for x in range(15):
        if maze[y][x]==1:
            canvas.create_rectangle(x*40,y*40,x*40+39,y*40+39,fill="skyblue",width=0)
            
label=tkinter.Label(font=("Times New Roman",80))
label.pack()
main_proc()
root.mainloop()






        

        
            
            
    
