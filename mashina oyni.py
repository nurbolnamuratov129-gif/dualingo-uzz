import turtle
import random

# --- Oyna sozlamalari ---
wn = turtle.Screen()
wn.title("Mashina o'yini")
wn.bgcolor("lightgrey")
wn.setup(width=600, height=600)
wn.tracer(0)

# --- Yo'l ---
road = turtle.Turtle()
road.hideturtle()
road.penup()
road.goto(-200, 300)
road.pendown()
road.fillcolor("darkgrey")
road.begin_fill()
for _ in range(2):
    road.forward(400)
    road.right(90)
    road.forward(600)
    road.right(90)
road.end_fill()

# --- Mashina ---
car = turtle.Turtle()
car.shape("square")
car.shapesize(stretch_wid=2, stretch_len=1)
car.color("blue")
car.penup()
car.goto(0, -250)

# --- To‘siqlar ---
obstacles = []

def create_obstacle():
    obs = turtle.Turtle()
    obs.shape("square")
    obs.shapesize(stretch_wid=2, stretch_len=1)
    obs.color("red")
    obs.penup()
    x = random.randint(-180, 180)
    y = 300
    obs.goto(x, y)
    obstacles.append(obs)

# --- Mashina boshqaruvi ---
def go_left():
    x = car.xcor()
    x -= 20
    if x > -200:
        car.setx(x)

def go_right():
    x = car.xcor()
    x += 20
    if x < 200:
        car.setx(x)

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# --- O'yin loop ---
score = 0
delay = 0.02

while True:
    wn.update()

    # To‘siqlarni yaratish
    if random.randint(1, 30) == 1:
        create_obstacle()

    # To‘siqlarni harakatlantirish
    for obs in obstacles:
        y = obs.ycor()
        y -= 10
        obs.sety(y)

        # To‘qnashuv
        if car.distance(obs) < 20:
            car.color("black")
            print("O'yin tugadi! Score:", score)
            wn.bye()
            break

        # Ekrandan chiqsa, o‘chirish
        if y < -300:
            obs.hideturtle()
            obstacles.remove(obs)
            score += 1

    # O'yin tezligi
    turtle.time.sleep(delay)
