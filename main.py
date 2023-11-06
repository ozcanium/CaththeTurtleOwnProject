import turtle
from random import random, randint
import time

CURSOR_SIZE = 20 #turtle size belirliyor. sabit

num = 0 #player puan saklar.başlangıç 0
def increase_score(): #puanı artıran fonk. num global kapsamda böylece fonk
    global num        #içindeki değişken dışarıdaki num ı değiştirebiliyor.
    num += 1

def my_turtle(color):  #rastgele renkli turtle oluşturuyor.

    length = randint(30, 100) #rastgele turtle size belirliyor.

    turtle_shape = turtle.Turtle('turtle', visible=False) #şekli ve görünmez olması  vs burda
    turtle_shape.shapesize(length / CURSOR_SIZE)
    turtle_shape.color(color)
    turtle_shape.penup()

    while True:
        nx = randint(-width // 2, width // 2)
        ny = randint(-height // 2, height // 2)

        turtle_shape.goto(nx, ny)

        for other_length, other_turtle in turtles:
            if turtle_shape.distance(other_turtle) < max(length, other_length):
                break
        else:
            break #turtle rastgele ekrana yansıtır. çakışıp çakışmadığını kontrol eder
            #çakışırsa tekrar ratgele yer seçer.

    turtle_shape.showturtle() #turtle ekranda gösterir. turtle gizleyen ve puan artıran fonk burda
    turtle_shape.onclick(lambda x, y, t=turtle_shape: (turtle_shape.hideturtle(), increase_score()))

    return length, turtle_shape #turtle oluşumu and ekran üzeri hareketleri döndürür.

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Speed Clicker")

width, height = screen.window_width(), screen.window_height()
#ekran özellikleri
turtles = [] #turtles saklandığı list

gameLength = 10
difficulty = 10
startTime = time.time() #game süre, zorluk, başlama zamanı
while True:
    time.sleep(5 / difficulty)

    rgb = (random(), random(), random())

    timeTaken = time.time() - startTime

    turtles.append(my_turtle(rgb))
    screen.title('SCORE: {}, TIME LEFT: {}'.format(num, int(round(gameLength - timeTaken, 0))))

    if time.time() - startTime > gameLength:
        break # oyunu başlatır. her turda belli bir süre bekliyor ve renk oluşturuyor.
        #süre hesaplama, ekran başlığını güncelleme, oluşan turtleı list ekler.

screen.title('FINISHED! FINAL SCORE: {}'.format(num))

screen.mainloop()
