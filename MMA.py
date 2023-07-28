# user input in class
class MMA:
    def __init__(self):
        self.name = input("Enter the fighter's name: ")
        self.promotion = input("Enter the promotion's name: ")
        self.age = int(input("Enter fighter's age: "))
        self.ring_name = input("Enter the fighter's ring name: ")

    def win(self):
        print("The {} won the match ".format(self.ring_name))

fighter_1 = MMA()  
fighter_1.win()