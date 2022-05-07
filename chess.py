import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
window = tk.Tk()
#!make classes  for pieces

fpBoard = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\board.png"
fpr = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\rook (b).png"
fpkn = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\knight (b).png"
fpb = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\bishop (b).png"
fpq = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\queen (b).png"
fpki = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\king (b).png"
fpp = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\pawn (b).png"
fpR = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\rook (w).png"
fpKn = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\knight (w).png"
fpB = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\bishop (w).png"
fpQ = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\queen (w).png"
fpKi = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\king (w).png"
fpP = r"C:\Users\astro\OneDrive\Documents\Pictures\ChessProgram\pawn (w).png"

#file paths for pieces(lower case is black,upper case is white)
#one square on the board is 47 pixels


canvas = Canvas(window, width = 376, height = 376)
canvas.pack()
imgBoard = ImageTk.PhotoImage(Image.open(fpBoard))  
canvas.create_image(0, 0, anchor=NW, image=imgBoard)
dragged = False

selectedPiece = ["",""]
capturedPiece =  ""
turn = "white"


class pawn:

    def __init__(self,x,y,fp,colour): #Constructor for the pawn class. Takes in the coords, colour and file path
        self.fp = fp
        self.x = x
        self.y = y
        self.colour = colour
        self.img = ImageTk.PhotoImage(Image.open(self.fp)) #Creates an image of the pawn 
        canvas.create_image(24 + (47*self.x), 24 + (47*self.y),anchor = CENTER, image = self.img)
       


    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def getColour(self):
        return self.colour

    def remove(self):
        self.img = canvas.delete()

    def move(self,x,y):
        self.x = x
        self.y = y
        self.img = ImageTk.PhotoImage(Image.open(self.fp))
        canvas.create_image(24 + (47*self.x), 24 + (47*self.y),anchor = CENTER, image = self.img)

    def validMove(self,x,y):
        if (self.colour== "black"  ): # Different sections for white and black since the white and black pawns in different directions
            if (y - self.y == 1 and self.x == x):  # Compares the attributes of the pawn to the new coord
                return True
            elif ( self.y == 1 and y - self.y == 2 and self.x == x): #Since pawns can move 2 if its their first move this checks if the pawn is in its startign position
                return True
            elif (y - self.y == 1 and abs(x - self.x) == 1 and board[y][x] != ""):  #Pawns can move diagonally if there is a piece 
                if (board[y][x].getColour() == "white"):  #Stops the pawn from moving on top of a piece with the same colour
                    return True
    

        elif(self.colour == "white" ):
            if (self.y - y == 1 and self.x == x): 
                return True
            elif ( self.y == 6 and self.y - y == 2 and self.x == x):
                return True
            elif (self.y - y == 1 and abs(self.x - x) == 1 and board[y][x] != ""):
                if (board[y][x].getColour() == "black"):
                    return True
          
        else:
            return False

    def blocked(self,x,y):
        if (abs(self.x - x) == 0):
            if(turn == "white" ):
                if abs(self.y-y) == 2:
                    for i in range(y,self.y,1):
                        if board[i][x] != "":
                            return True
                            break
                    
                elif abs(self.y-y) == 1:
                    if board[y][x] != "":
                        return True
                    else:
                        return False
            elif (turn == "black"  ):
                if abs(self.y-y) == 2:
                    for i in range(y,self.y,1):
                        if board[i][x] != "":
                            return True
                    
                elif abs(self.y-y) == 1:
                    if board[y][x] != "":
                        return True
                    else:
                        return False
        elif (abs(self.x - x) == 1 and abs(self.y - y) == 1):
            if board[y][x] != "":
                if board[y][x].getColour() == self.colour:
                    return True
                else:
                    return False
            else :
                return False
        else:
            return False
            


class knight(pawn):
    def __init__ (self,x,y,fp,colour):
        super().__init__ (x,y,fp,colour)
            
    def validMove(self,x,y):
        if ((abs(self.x-x)== 1 and abs(self.y-y)==2) or (abs(self.x-x)== 2 and abs(self.y-y)==1) ):
            return True
        else:
            return False

    def blocked(self,x,y):
        if board[y][x] != "":
            if self.colour == board[y][x].getColour() :
                return True
            else:
                return False


class bishop(pawn):
    def __init__ (self,x,y,fp,colour):
        super().__init__ (x,y,fp,colour)
            
    def validMove(self,x,y):
        if ((abs(self.x-x) == abs(self.y-y))):
            return True
        else:
            return False

    def blocked(self,x,y):
        blocked = False
        xIndex = 0
        yIndex = 0

        checky = self.y
        checkx = self.x

        if self.x > x:
            xIndex = -1
        elif self.x < x:
            xIndex = 1

        if self.y > y:
            yIndex = -1
        elif self.y < y:
            yIndex = 1    

      
        if board[y][x] != "":
            if board[y][x].getColour() == self.colour: 
                    blocked = True

        if board[y][x] == "":
            for i in range(self.x,x,xIndex):
                checky += yIndex
                checkx += xIndex
                if board[checky][checkx] != "":
                    blocked = True
                    break

        return blocked            

    

class rook(pawn):
    def __init__ (self,x,y,fp,colour):
        super().__init__ (x,y,fp,colour)


    def validMove(self,x,y):
        if ((self.x!= x and self.y == y) or(self.x== x and self.y != y) ):
            return True
        else:
            return False
    def blocked(self,x,y): #error prevents capture
        index = 0
        blocked = False
        if self.x - x != 0:
            if self.x > x:
                index = -1
            elif self.x < x:
                index = 1

            if board[y][x] != "":
                if board[y][x].getColour() == self.colour: 
                    blocked = True
                
            if board[y][x] == "":
                for i in range(self.x,x,index):
                    if board[y][i+index] != "":
                        blocked = True
                        break
                    
            
               
                
        elif self.y - y != 0:
            if self.y > y:
                index = -1
            elif self.y < y:
                index = 1

            if board[y][x] != "":
                if board[y][x].getColour() == self.colour: 
                    blocked = True

            if board[y][x] == "":
                for i in range(self.y,y,index):
                    if board[i+index][x] != "":
                        blocked = True
                        break

        return blocked
        

class queen(pawn):
    def __init__ (self,x,y,fp,colour):
        super().__init__ (x,y,fp,colour)


    def validMove(self,x,y):
        if ((self.x != x and self.y == y) or(self.x == x and self.y != y) or (abs(self.x-x) == abs(self.y-y))):
            return True
        else:
            return False

    def blocked(self,x,y): #error queen can move through pawn if it is 1 space b4 final y
        blocked = False
        if (self.y == y or self.x == x):
            if self.x - x != 0:
                if self.x > x:
                    index = -1
                elif self.x < x:
                    index = 1

                if board[y][x] != "":
                    if board[y][x].getColour() == self.colour: 
                        blocked = True
                    
                if board[y][x] == "":
                    for i in range(self.x,x,index):
                        if board[y][i+index] != "":
                            blocked = True
                            break
                    
            
               
                
            elif self.y - y != 0:
                if self.y > y:
                    index = -1
                elif self.y < y:
                    index = 1

                if board[y][x] != "":
                    if board[y][x].getColour() == self.colour: 
                        blocked = True

                if board[y][x] == "":
                    for i in range(self.y,y,index):
                        if board[i+index][x] != "":
                            blocked = True
                            break


        elif (abs(self.x - x) == abs(self.y - y)):
           
            xIndex = 0
            yIndex = 0

            checky = self.y
            checkx = self.x

            if self.x > x:
                xIndex = -1
            elif self.x < x:
                xIndex = 1

            if self.y > y:
                yIndex = -1
            elif self.y < y:
                yIndex = 1    

          
            if board[y][x] != "":
                if board[y][x].getColour() == self.colour: 
                        blocked = True

            if board[y][x] == "":
                for i in range(self.x,x,xIndex):
                    checky += yIndex
                    checkx += xIndex
                    if board[checky][checkx] != "":
                        blocked = True
                        break

            

        return blocked            





class king(pawn):
    def __init__ (self,x,y,fp,colour):
        super().__init__ (x,y,fp,colour)


    def validMove(self,x,y):
        if ((abs(self.x-x)== 1 and abs(self.y-y)<=1) or (abs(self.x-x)<= 1 and abs(self.y-y)==1) ):
            return True
        else:
            return False
    def blocked(self,x,y):
        if board[y][x] != "":
            if self.colour == board[y][x].getColour() :
                return True
            else:
                return False

#White pieces
P1 = pawn(0,6,fpP,"white")
P2 = pawn(1,6,fpP,"white")
P3 = pawn(2,6,fpP,"white")
P4 = pawn(3,6,fpP,"white")
P5 = pawn(4,6,fpP,"white")
P6 = pawn(5,6,fpP,"white")
P7 = pawn(6,6,fpP,"white")
P8 = pawn(7,6,fpP,"white")
Kn1 = knight(1,7,fpKn,"white")
Kn2 = knight(6,7,fpKn,"white")
B1 = bishop(2,7,fpB,"white")
B2 = bishop(5,7,fpB,"white")
R1 = rook(0,7,fpR,"white")
R2 = rook(7,7,fpR,"white")
Q1 = queen(3,7,fpQ,"white")
Ki1 = king(4,7,fpKi,"white")
#Black pieces
p1 = pawn(0,1,fpp,"black")
p2 = pawn(1,1,fpp,"black")
p3 = pawn(2,1,fpp,"black")
p4 = pawn(3,1,fpp,"black")
p5 = pawn(4,1,fpp,"black")
p6 = pawn(5,1,fpp,"black")
p7 = pawn(6,1,fpp,"black")
p8 = pawn(7,1,fpp,"black")
kn1 = knight(1,0,fpkn,"black")
kn2 = knight(6,0,fpkn,"black")
b1 = bishop(2,0,fpb,"black")
b2 = bishop(5,0,fpb,"black")
r1 = rook(0,0,fpr,"black")
r2 = rook(7,0,fpr,"black")
q1 = queen(3,0,fpq,"black")
ki1 = king(4,0,fpki,"black")#

board = [[r1,kn1,b1,q1,ki1,b2,kn2,r2],
         [p1,p2,p3,p4,p5,p6,p7,p8],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["","","","","","","",""],
         [P1,P2,P3,P4,P5,P6,P7,P8],
         [R1,Kn1,B1,Q1,Ki1,B2,Kn2,R2]]


def capture(capturedPiece):
    if capturedPiece != "":
        capturedPiece.remove()



def drag(e):
    global dragged
    x = e.x//47 #stores to coordinates of the users clicks
    y = e.y//47
    if(board[y][x] != ""): # makes sure the user is not clicking on a blank square
        selectedPiece[0] = board[y][x] #selects the piece where the user clicked
        if selectedPiece[0].getColour() == turn: #only allows a piece to be selected if the colour matches the turn
                dragged = True

def release(e):
    global dragged
    global turn
    if dragged:
        x = e.x//47 #stores to coordinates of the users clicks
        y = e.y//47
        capturedPiece = board[y][x] #find the contents of the square where the piece lands
        if selectedPiece[0] != "":
            if selectedPiece[0].validMove(x,y) and not selectedPiece[0].blocked(x,y):
                if x >= 0  and x <= 7 and y >= 0  and y <= 7: #Makes sure the piece isn't moved off the board
                    board[selectedPiece[0].getY()][selectedPiece[0].getX()] = "" #updates the current index of the piece in the array to ""
                    capture(capturedPiece) #Calls capture function
                    selectedPiece[0].move(x,y)#coordinates have been edited using the formula i created at the start of the iteration
                    board[y][x] = selectedPiece[0]
                    if selectedPiece[0].getColour() == "white": #swaps the colour of the turn based on the colour of the piece that moved
                        turn = "black"
                        
                    elif selectedPiece[0].getColour() == "black":
                        turn = "white"
                        
        
    dragged = False

canvas.bind("<Button-1>", drag)
canvas.bind("<ButtonRelease-1>", release)

            
