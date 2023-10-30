class Elevator:
    def __init__(self, top_floors: int, bottom_floors: int):
        self.top_floors = top_floors
        self.bottom_floors = bottom_floors
        self.current_floor = self.bottom_floors

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

    def get_floor_name(self):
        print(f"You are currently at floor {self.current_floor}")


if __name__ == "__main__":
    h = Elevator(10, -1)
    h.go_to_floor(5)
    h.get_floor_name()
    h.go_to_floor(-10)
