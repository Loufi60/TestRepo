import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):
    x = round(r * math.cos(math.radians(theta)), 5)
    y = round(r * math.sin(math.radians(theta)), 5)
    print(f"The Cartesian coordinates are ({x}, {y})")
    return (x, y)


#input from the user
print("Function 1:")
r = float(input("What is the radius r? "))
theta = float(input("What is the angle θ (in degrees)? "))
polar_to_cartesian(r, theta)



# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r = round(math.sqrt(x**2 + y**2), 5)
    theta = round(math.degrees(math.atan2(y, x)), 5)
    print(f"The polar coordinates are ({r}, {theta}), where θ is in degrees")
    return (r, theta)
    
    
#input from the user
print("Function 2:")
x = float(input("What is the x coordinate? ")) 
y = float(input("What is the y coordinate? "))
cartesian_to_polar(x, y)


# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    x = round(A * math.cos(2 * math.pi * f * t + math.radians(phi)), 5)
    print(f"The position of the pendulum at time {t} seconds is {x}")
    return x
#input from the user
print("Function 3:")
A = float(input("What is the amplitude A? "))
f = float(input("What is the frequency f? "))
phi = float(input("What is the phase ϕ (in degrees)? "))
t = float(input("What is the time t (in seconds)? "))
pendulum_position(A, f, phi, t)