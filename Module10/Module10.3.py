class Elevator:
    def __init__(self, top_floors: int, bottom_floors: int):
        self.top_floors = top_floors
        self.bottom_floors = bottom_floors
        self.current_floor = self.bottom_floors

    def get_current_floor_number(self):
        return self.current_floor

    def go_to_floor(self, floor_number: int):
        # going up operation
        if floor_number > self.current_floor:
            while self.current_floor != floor_number and self.current_floor <= self.top_floors:
                self.floor_up()
                print(f"You are going up the floor  {self.current_floor}")

        # going down operation
        if floor_number < self.current_floor:
            while self.current_floor != floor_number and self.current_floor > self.bottom_floors:
                self.floor_down()
                print(f"You are going down the floor {self.current_floor}")

    def floor_up(self):
        self.current_floor = self.current_floor + 1

    def floor_down(self):
        self.current_floor = self.current_floor - 1


class Building:
    def __init__(self, no_of_top_floors, no_of_bottom_floors, no_of_elevators):
        self.no_of_top_floors = no_of_top_floors
        self.no_of_bottom_floors = no_of_bottom_floors
        self.no_of_elevators = no_of_elevators
        self.elevator_list = []
        for i in range(1, self.no_of_elevators):
            self.elevator_list.append(Elevator(no_of_top_floors,no_of_bottom_floors))

    def run_elevator(self, elevator_number: int, destination_floor: int):
        self.elevator_list[elevator_number - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in range(1, len(self.elevator_list)):
            self.elevator_list[elevator].go_to_floor(self.no_of_bottom_floors)

        print("All elevators of your building are now at the bottom floor because of an fire alarm.")


if __name__ == "__main__":

    my_building = Building(9, -2, 6)

    # moving some elevators of building to up and down floors.
    my_building.run_elevator(2, 6)
    my_building.run_elevator(3, 4)

    #fire alarm
    my_building.fire_alarm()

    #checking current floor of random elevator
    print(my_building.elevator_list[2].current_floor)
