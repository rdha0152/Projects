#PROJECT: INTERACTIVE STORYBOOK -TURTLE PYTHON

import turtle
import random
import time 
global NotStarted
global NotStarted1
global NotStarted2
global house1
global house2
global redcar
global bluecar

grape_dictionary = {}


def load_words1():
  
  file = open('grapefile')
  list = []
  for line in file:
    
    list.append(line)
  return list
facts_questions = load_words1()

def load_answers1():
  file = open('grapeanswers')
  list3 = []
  list4 = []
  for line in file:
    
    list3.append(line)
  for line in list3:
    line.strip()
    list4.append(line)
  return list4
facts_answers = load_answers1()
def grape_riddles():
  file = open('riddles')
  list = []
  
  for line in file:
    
    list.append(line)
  
  return list
riddle_list = grape_riddles()
grape_dictionary = dict(zip(facts_questions, facts_answers))

  
print("I’m round but I’m not a ball")
response = str(input('What am I? '))
response = response.lower()
while response != 'grape':
  if response != 'grape':
    for i in riddle_list[1:]:
    
      print('Incorrect.')
      print(i)
      response = str(input('What am I? '))
      response = response.lower()

print("Congratulations! You've earned some random facts about grapes!")
    

response2 = int(input("Enter a number 1-5: "))
while response2 in range(1,4):
  for key in grape_dictionary.items():
    print(key)
    response2 = int(input("Enter a number 1-5: "))

print("I know a grape who spends his time sitting in the sun.")
print("It's his raisin d'etre!")
print("You've unlocked the story!")


def stall():
  tt = turtle.Turtle()
  tt.hideturtle()
  tt.penup()
  tt.speed(1)
  tt.forward(600) 

#######TITLE PAGE#########
s = turtle.Screen()  
s = turtle.Screen()
s.title("Raisin Together")    

#Sets up button Turtle VINEYARDS
vineyards = turtle.Turtle()
turtle.addshape('ihopeitsgrapes.gif')
vineyards.shape('ihopeitsgrapes.gif')
vineyards.penup()
vineyards.goto(0,50)
s.bgpic('realdirtgrass.gif')

##Starting Text
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(0, 100)
text.color("black")
text.write("Click the grapes!", False, align='center', font=('Arial', 25, 'bold'))

x = 0
y = 50
def start(x, y):
  global NotStarted
  NotStarted = False
  s.clearscreen()
  
NotStarted = True

while NotStarted:
  vineyards.onclick(start)



######### START OF STORY######

s.bgpic('realdirtgrass.gif')
grape1 = turtle.Turtle() 
grape2 = turtle.Turtle()
hand = turtle.Turtle()
water = turtle.Turtle()
sprout = turtle.Turtle()
turtle.addshape('sprout.gif')
turtle.addshape('grape1.gif')
turtle.addshape('grape2.gif')
turtle.addshape('hand.gif')
turtle.addshape('water.gif')

grape1.hideturtle()
grape1.shape('grape1.gif')
grape2.shape('grape2.gif')
grape2.hideturtle()
hand.shape('hand.gif')
hand.goto(200,-175)
text.write("Plant the Seed!", False, align='center', font=('Arial', 25, 'bold'))
stall()
hand.showturtle()
text.clear()
water.shape('water.gif')
water.goto(-200,-175)
text.write("Water the Seed!", False, align='center', font=('Arial', 25, 'bold'))
stall()
text.clear()

#PLANTS THE SEED
s.listen()
def handwater(x,y):
  hand.goto(0,-50)
  #stall()
  hand.hideturtle()
hand.onclick(handwater)
#WATERS THE PLANT
def waterseed(x,y):
  water.goto(0,0)
  stall()
  water.hideturtle()
  sprout.goto(0,0)
  sprout.shape('sprout.gif')
  stall()
  
  grape1.goto(0,-200)
  stall()
  
water.onclick(waterseed)
text.write("This is the story,", False, align='center', font=('Arial', 25, 'bold'))
stall()
text.clear()
text.write("of two grapes,", False, align='center', font=('Arial', 25, 'bold'))
stall()
text.clear()
text.write("growing up together!", False, align='center', font=('Arial', 25, 'bold'))
stall()

s = turtle.getscreen()

t_text = turtle.Turtle()
t_text.penup()
t_text.hideturtle()




######School Period####

s.clearscreen()
s = turtle.Screen()  
s = turtle.Screen()
s.title("Raisin Together")    



bgrape1 = turtle.Turtle()
bgrape2 = turtle.Turtle()
turtle.addshape('grape1.gif')
turtle.addshape('grape1.gif')
bgrape1.shape('grape1.gif')
bgrape1.penup()
bgrape1.goto(0,-200)
turtle.addshape('grape2.gif')
turtle.addshape('grape2.gif')
bgrape2.shape('grape2.gif')
bgrape2.penup()
bgrape2.goto(100,-200)
s.bgpic('classroom.gif')


def mathquestion():
  text = turtle.Turtle()
  text.penup()
  text.hideturtle()
  text.goto(40, 130)
  text.color("black")
  text.write("1 + 1?", False, align='right', font=('Arial', 20, 'bold'))

  
mathquestion()



def two(x,y):
  text = turtle.Turtle()
  text.penup()
  text.hideturtle()
  text.goto(-150, 90)
  text.color("black")
  text.write("Correct!", False, align='center', font=('Arial', 20, 'bold'))
  

twoo = turtle.Turtle()
turtle.addshape("2.gif")
twoo.shape("2.gif")
twoo.penup()
twoo.goto(-130, 20)

twoo.onclick(two)

def eleven11(x,y):
  
  text = turtle.Turtle()
  text.penup()
  text.hideturtle()
  text.goto(0, 90)
  text.color("black")
  text.write("Wrong!", False, align='center', font=('Arial', 20, 'bold'))



eleven = turtle.Turtle()
turtle.addshape("11.gif")
eleven.shape("11.gif")
eleven.penup()
eleven.goto(-5, 20)

eleven.onclick(eleven11)

def three3(x,y):
  
  text = turtle.Turtle()
  text.penup()
  text.hideturtle()
  text.goto(130, 90)
  text.color("black")
  text.write("Wrong!", False, align='center', font=('Arial', 20, 'bold'))


  
three = turtle.Turtle()
turtle.addshape("3.gif")
three.shape("3.gif")
three.penup()
three.goto(120, 20)
three.onclick(three3)



stall()
stall()
stall()
time.sleep(5)

s.clearscreen()

def stall2():
  tt = turtle.Turtle()
  tt.hideturtle()
  tt.penup()
  tt.speed(1)
  tt.forward(100) 

  
s = turtle.Screen()


grape1grad = turtle.Turtle() 
grape2grad = turtle.Turtle()
grape1lunch = turtle.Turtle() 
grape2lunch = turtle.Turtle()
grape1uic = turtle.Turtle()
grape2uic = turtle.Turtle()
grape1house = turtle.Turtle()
grape2house = turtle.Turtle()
grape1family = turtle.Turtle()
grape2family = turtle.Turtle()
cap1 = turtle.Turtle()
cap2 = turtle.Turtle()
confetti = turtle.Turtle()
confetti2 = turtle.Turtle()


turtle.addshape("grape1.gif")
turtle.addshape('grape2.gif')
turtle.addshape('graduationcap.gif')
turtle.addshape('confetti.gif')
confetti.shape('confetti.gif')
confetti2.shape('confetti.gif')
confetti2.hideturtle()
confetti.hideturtle()
text = turtle.Turtle()
text.penup()
text.goto(0, 100)
text.color("black")
text.write("But at graduation,", False, align='center', font=('Arial', 25, 'bold'))
stall()
text.clear()
text.write("Everything changes.", False, align='center', font=('Arial', 25, 'bold'))
stall()
text.clear()
grape1grad.shape('grape1.gif')
grape2grad.shape('grape2.gif')
cap1.shape('graduationcap.gif')
cap1.penup()
cap1.goto(0,50)
cap2.shape('graduationcap.gif')
cap2.penup()
cap2.goto(-100,50)
grape1grad.penup()
grape2grad.penup()
grape1grad.goto(-100,0)
s.bgpic('graduation.gif')
x = 0
y = 50
def start(x, y):
  global NotStarted
  NotStarted = False
  cap1.goto(0,200)
  cap2.goto(-100,200)
  confetti.penup()
  confetti.showturtle()
  confetti.goto(0,0)
  stall()
  s.clearscreen()
  
NotStarted = True

while NotStarted:
  cap1.onclick(start)

s.clearscreen()
grape1lunch.shape('grape1.gif')
grape2lunch.shape('grape2.gif')
grape1lunch.hideturtle()
grape2lunch.hideturtle()
def slideuic():
  grape1lunch.penup()
  grape2lunch.penup()
  grape1lunch.showturtle()
  grape2lunch.showturtle()
  grape1lunch.goto(100,0)
  grape2lunch.goto(0,0)
  s.bgpic('lunch.gif')
  text = turtle.Turtle()
  text.penup()
  
  text.goto(0, 100)
  text.color("white")
  text.write("They start UIC together!", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("They study together,", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("Eat lunch together,", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("Complain about their CS classes,", False, align='center', font=('Arial', 25, 'bold'))
  
  stall()
  text.clear()
  s.clearscreen()
slideuic()


grape1uic.shape('grape1.gif')
grape2uic.shape('grape2.gif')
grape1uic.hideturtle()
grape2uic.hideturtle()

def uicgrad():
  s.bgpic('finally.gif')
  ring = turtle.Turtle()
  ring.hideturtle()
  turtle.addshape('ring.gif')
  ring.shape('ring.gif')
  ring.goto(50,50)
  grape1uic.penup()
  grape2uic.penup()
  grape1uic.showturtle()
  grape2uic.showturtle()
  grape1uic.goto(100,0)
  grape2uic.goto(0,0)
  text = turtle.Turtle()
  text.penup()
  
  text.goto(0, 100)
  text.color("white")
  text.write("But they somehow,", False, align='center', font=('Arial', 25, 'bold'))
  stall2()
  text.clear()
  text.write("Manage to graduate!,", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("And one grapes asks,", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("the other an important question,", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("Will you marry me?", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  ring.showturtle()
  text.clear()
  text.write("And of course,", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("The other grape accepts.", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  
  
  stall()
  s.clearscreen()
uicgrad()
NotStarted1 = True
def start2(x, y):
  global NotStarted1
  global house2
  global house1
  NotStarted1 = False
  s.bgpic('bighouse1.gif')
  house2.hideturtle()
  house1.hideturtle()
  grape1house.shape('grape1.gif')
  grape2house.shape('grape2.gif')
  grape1house.penup()
  grape2house.penup()
  grape1house.goto(-50,-50)
  grape2house.goto(-150,-50)
  
  stall()
  
def start3(x, y):
  global house1
  global house2
  global NotStarted1
  NotStarted1 = False
  s.bgpic('bighouse2.gif')
  house1.hideturtle()
  house2.hideturtle()
  grape1house.shape('grape1.gif')
  grape2house.shape('grape2.gif')
  grape1house.penup()
  grape2house.penup()
  grape1house.goto(-50,-50)
  grape2house.goto(-150,-50)
  stall()
  
  
def choosehouse():
  global house1
  global house2
  text = turtle.Turtle()
  text.penup()
  
  text.goto(0, 100)
  text.color("black")
  text.write("They start a life together!", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  
  text.write("Pick a house!", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  
  #text.showturtle()
  house1 = turtle.Turtle()
  house2 = turtle.Turtle()
  turtle.addshape('house1.gif')
  turtle.addshape('house2.gif')
  house1.shape('house1.gif')
  house2.shape('house2.gif')
  house1.penup()
  house2.penup()
  
  house1.goto(-100,0)
  house2.goto(100,0)
  
  while NotStarted1:
    house1.onclick(start2)
    
    house2.onclick(start3)
    
    stall()
    
choosehouse()


NotStarted2 = True
def start4(x, y):
  global NotStarted2
  global redcar
  global bluecar
  NotStarted2 = False
  redcargrape = turtle.Turtle()
  turtle.addshape('redcargrape.gif')
  redcar.hideturtle()
  bluecar.hideturtle()
  redcargrape.hideturtle()
  redcargrape.shape('redcargrape.gif')
  redcargrape.penup()
  redcargrape.goto(500,-75)
  redcargrape.showturtle()
  stall()
  redcargrape.goto(-350,-50)
  stall()

def start5(x, y):
  global redcar
  global bluecar
  global NotStarted2
  NotStarted2 = False
  bluecargrape = turtle.Turtle()
  turtle.addshape('bluecargrape.gif')
  redcar.hideturtle()
  bluecar.hideturtle()
  bluecargrape.hideturtle()
  bluecargrape.shape('bluecargrape.gif')
  bluecargrape.penup()
  bluecargrape.goto(-100,-75)
  bluecargrape.showturtle()
  
  stall()
  
  bluecargrape.goto(550,-50)
  stall()
  

def choosecar():
  global redcar
  global bluecar
  global NotStarted2
  s.clearscreen()
  s.bgpic('cardealership.gif')
  text = turtle.Turtle()
  text.penup()
  
  text.goto(0, 100)
  text.color("black")
  
  text.write("They buy a car together", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("Pick a car!", False, align='center', font=('Arial', 25, 'bold'))
  bluecar = turtle.Turtle()
  redcar = turtle.Turtle()
  turtle.addshape('bluecar.gif')
  turtle.addshape('redcar.gif')
  bluecar.shape('bluecar.gif')
  redcar.shape('redcar.gif')  
  bluecar.penup()
  redcar.penup()
  bluecar.goto(-100,-75)
  redcar.goto(100,-75)  
  
  
  
  while NotStarted2:
    redcar.onclick(start4)
    
    bluecar.onclick(start5)

    stall()
choosecar()

  
def family():
  s.clearscreen()
  s.bgpic('vineyardimg.gif')
  text = turtle.Turtle()
  text.penup()
  
  text.goto(0, 100)
  text.color("black")
  circle = turtle.Turtle()
  grape1family.shape('grape1.gif')
  grape2family.shape('grape2.gif')
  grape1family.penup()
  grape2family.penup()
  grape1family.goto(50,0)
  grape2family.goto(150,0)
  
  text.write("And have many grape..", False, align='center', font=('Arial', 25, 'bold'))
  stall()
  text.clear()
  text.write("Surprises!!!", False, align='center', font=('Arial', 25, 'bold'))
  
  for i in range(20):
    r =random.randint(-100,0)
    d = random.randint(-100,0)
    radius = 10
    circle.up()
    if r < -50:
      circle.goto(d,r)
    if d < -50:
      circle.goto(r,d)
    circle.down()
    circle.begin_fill()
    circle.circle(radius)
    circle.fillcolor('purple')
    circle.end_fill()
  stall()
  text.clear()
  text.write("Until later they..", False, align='center', font=('Arial', 25, 'bold'))
  stall()
family() 

def theend():
  s.clearscreen()
  s.bgpic('later.gif')
  stall()
  s.clearscreen()
  s.bgpic('raisinsold.gif')
theend()


s.mainloop()
