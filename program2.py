class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change >= 0:
            self.current_speed = min(self.current_speed + speed_change, self.max_speed)
        else:
            self.current_speed = max(self.current_speed + speed_change, 0)


if __name__ == "__main__":

    new_car = Car("ABC-123", 142)


    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)


    print("Current Speed:", new_car.current_speed, "km/h")


    new_car.accelerate(-200)


    print("Final Speed after emergency brake:", new_car.current_speed, "km/h")
