import turtle
import tkinter as tk

# User inputs for car dimensions
length = float(input("Enter car length(20-40): "))
width = float(input("Enter car width(30-40): "))
height = float(input("Enter car height(20-40): "))
weight = float(input("Enter car weight(20-40): "))

# Constants
SLOPE = 0.20
MAX_SPEED = 35
ACCELERATION = 5
FRICTION_COEFFICIENT = 5

# Set up the screen and turtle
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor("lightblue")
screen.title("Car Simulation")

# turtle_pen = turtle.Turtle()
turtle_car = turtle.Turtle(shape='square')
turtle_car.shapesize(length/20, width/20, outline=1)
turtle_car.color("red")

turtle_car.penup()
turtle_car.setpos(-screen.window_width() / 2, -screen.window_height() / 2)
turtle_car.pendown()

# Initialize variables
speed = 11
distance = -screen.window_width() / 2 

time_elapsed = 0
road_type = 'smooth'
weather_type = 'normal'
slope_direction = 1

# Define functions to update road and weather settings


def update_road_type(road):
    global road_type
    road_type = road


def update_weather_type(weather):
    global weather_type
    weather_type = weather


# Create buttons to update road and weather settings
road_button_smooth = tk.Button(
    text='Smooth Road', command=lambda: update_road_type('smooth'))
road_button_smooth.pack(side=tk.LEFT)

road_button_rough = tk.Button(
    text='Rough Road', command=lambda: update_road_type('rough'))
road_button_rough.pack(side=tk.LEFT)

weather_button_normal = tk.Button(
    text='Normal Weather', command=lambda: update_weather_type('normal'))
weather_button_normal.pack(side=tk.LEFT)

weather_button_snow = tk.Button(
    text='Snow Weather', command=lambda: update_weather_type('snow'))
weather_button_snow.pack(side=tk.LEFT)

weather_button_rain = tk.Button(
    text='Rain Weather', command=lambda: update_weather_type('rain'))
weather_button_rain.pack(side=tk.LEFT)


# Simulation loop
while True:
    # Update speed based on road and weather settings
    if road_type == 'smooth':
        speed = min(speed + ACCELERATION, MAX_SPEED)
    elif road_type == 'rough':
        speed = max(speed - FRICTION_COEFFICIENT, 0)

    if weather_type == 'snow':
        speed *= 0.5
    elif weather_type == 'rain':
        speed *= 0.75

    # Update position based on speed and slope
    turtle_car.setx(distance)
    turtle_car.sety(distance * SLOPE * slope_direction)

    # Update time elapsed and distance traveled
    time_elapsed += 0.1
    distance += speed * 0.1

    # Check if car has reached end of hill
    if distance >= 0 and slope_direction > 0:
        slope_direction = -1

    # Update the screen
    screen.update()
    turtle_car.speed(0)

    # Check if car has reached end of screen
    if distance >= screen.window_width() / 2:
        break

# Print time elapsed and wait for user to close the window
print(f"Time elapsed: {time_elapsed:.1f} seconds")
screen.mainloop()
