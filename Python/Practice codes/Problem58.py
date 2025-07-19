from random import randint
class Train() :
    def __init__(self, trainno, seatno):
        self.trainno = trainno 
        self.seatno = seatno
    def ticketbook(self, trainno, seatno ,fro, to):
        print(f"Your train seat is booked in {self.trainno} in {self.seatno} which is going {fro} to {to}.")
    def fare(self, trainno, seatno, fro, to):
        print(f"Your fare for going from {fro} to {to} in {self.trainno} whie seating on {self.seatno} is {randint(333,555)}")
    def status(self, trainno):
        print(f"your train {self.trainno} is comming on time")

t = Train(179425, "11A")
t.ticketbook(179425, "11A", "Chandigrh", "Goa")
t.fare(179425, "11A", "Chandigrh", "Goa")
t.status(179425)