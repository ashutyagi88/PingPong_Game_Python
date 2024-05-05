from turtle import Turtle
ALIGN = "center"
FONT_FAMILY = "Times New Roman"
FONT_SIZE = 50
FONT_WEIGHT = "bold"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.netting()
        self.playerOne = 0
        self.playerTwo = 0
        self.update_score()

    def netting(self):
        net = Turtle("square")
        net.speed(0)
        net.goto(0,400)
        net.color("white")
        net.penup()
        net.setheading(270)
        net.width(2.5)
        net.hideturtle()
        while(net.ycor() != -400):
            net.pendown()
            net.forward(20)
            net.penup()
            net.forward(20)
    
    def update_score(self):
        self.clear()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed(0)
        self.goto(-325,375)
        self.write(f"{self.playerOne}",False,align=ALIGN,font=(FONT_FAMILY,FONT_SIZE,FONT_WEIGHT))
        self.goto(325,375)
        self.write(f"{self.playerTwo}",False,align=ALIGN,font=(FONT_FAMILY,FONT_SIZE,FONT_WEIGHT))

    def playerOnePt(self):
        self.playerOne += 1
        self.update_score()

    def playerTwoPt(self):
        self.playerTwo += 1
        self.update_score()
    
    def game_over(self,player):
        if(player == 1):
            self.goto(-300,0)
        else:
            self.goto(300,0)
        self.write(f"Player {player} Won.",False,align=ALIGN,font=(FONT_FAMILY,FONT_SIZE,FONT_WEIGHT))