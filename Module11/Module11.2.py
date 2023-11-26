class Car:

    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def drive(self, hour):
        dist_covered = self.current_speed * hour
        self.distance = self.distance + dist_covered
        print(
            f"The distance travelled for car with registration {self.reg_number} with speed {self.current_speed} km/h is {self.distance} km.")

    def accelerate(self, speed: int):
        if self.max_speed < self.current_speed + speed:
            self.current_speed = self.max_speed
        elif self.current_speed + speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed + speed


class ElectricCar(Car):

    def __init__(self, reg_number, max_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(reg_number, max_speed)

    def get_max_speed(self):
        print(f"Maximum speed of car is {self.max_speed}")


class GasolineCar(Car):

    def __init__(self, reg_number, max_speed, tank_volume):
        self.tank_volume = tank_volume
        super().__init__(reg_number, max_speed)

    def get_max_speed(self):
        print(f"Maximum speed of car is {self.max_speed}")


selected_ElectricCar_speed = 100
selected_GasolineCar_speed = 90
given_time = 3
electric_car_1 = ElectricCar("ABC-15", 180, 52.5)
gasoline_car_1 = GasolineCar("ACD-123", 165, 32.3)

electric_car_1.accelerate(selected_ElectricCar_speed)
gasoline_car_1.accelerate(selected_GasolineCar_speed)
gasoline_car_1.drive(given_time)
print()
electric_car_1.drive(given_time)
