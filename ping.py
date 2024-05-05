from turtle import Turtle

class Ping(Turtle):
    def __init__(self):
        super().__init__()
        self.playersList = []
        self.playerOne()
        self.playerTwo()
     
    def makePlayer(self,position):
        player = Turtle("square")
        player.color("white")
        player.shapesize(9,1.5)
        player.penup()
        player.goto(position)
        self.playersList.append(player)
    
    def playerOne(self):
        self.makePlayer((-600,0))
    
    def playerTwo(self):
        self.makePlayer((600,0))
    
    def moveUpPlayerOne(self):
        if(self.playersList[0].ycor() != 360):
            new_y = self.playersList[0].ycor() + 30
            self.playersList[0].goto(self.playersList[0].xcor(),new_y)

    def moveUpPlayerTwo(self):
        if(self.playersList[1].ycor() != 360):
            new_y = self.playersList[1].ycor() + 30
            self.playersList[1].goto(self.playersList[1].xcor(),new_y)

    def moveDownPlayerOne(self):
        if(self.playersList[0].ycor() != -360):
            new_y = self.playersList[0].ycor() - 30
            self.playersList[0].goto(self.playersList[0].xcor(),new_y)

    def moveDownPlayerTwo(self):
        if(self.playersList[1].ycor() != -360):
            new_y = self.playersList[1].ycor() - 30
            self.playersList[1].goto(self.playersList[1].xcor(),new_y)

        
        

        
    