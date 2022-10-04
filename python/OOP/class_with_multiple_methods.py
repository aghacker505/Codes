class Phone:
    def set_color(self, color):
        self.color = color
    def set_cost(self, cost):
        self.cost = cost
    def get_color(self):
        return self.color
    def get_cost(self):
        return self.cost
    def make_call(self):
        print("Calling...")
    def play_games(self):
        print("Playing games...")

p1 = Phone()
p1.set_color('Green')
p1.set_cost(100)
print(p1.get_color())
print(p1.get_cost())
p1.make_call()
p1.play_games()