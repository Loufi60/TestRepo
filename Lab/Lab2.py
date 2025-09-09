# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # TODO: Implement this function

    # Output the height at time t
    h_t = h0 - 4.9*t**2
    print(f"Height of the ball at time {t} second = {h_t} meters")

# Input from the user
print("Problem 1.1")
h0 = float(input("Enter initial height: "))
t = float(input("Enter time: "))
calculate_height(h0, t)

print("Problem 1.2")
h0 = float(input("Enter initial height: "))
t = float(input("Enter time: "))
calculate_height(h0, t)

print("Problem 1.3")
h0 = float(input("Enter initial height: "))
t = float(input("Enter time: "))
calculate_height(h0, t)

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    
    # Output the distance traveled by the car
    print(f"The car will travel {distance} meters in {t} seconds.")

# Input from the user
print("Problem 2.1")
t = float(input("Enter time: "))
Speed = 20
distance = Speed * t
calculate_car_distance(t)

print("Problem 2.2")
t = float(input("Enter time: "))
Speed = 20
distance = Speed * t
calculate_car_distance(t)

print("Problem 2.3")
t = float(input("Enter time: "))
Speed = 20
distance = Speed * t
calculate_car_distance(t)



 