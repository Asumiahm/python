def to_kg(weight):
    return weight+10
def to_lbs(weight):
    return weight/10
class FindMax:
   def __init__(self,numbers):
    self.numbers=numbers
   def maxi(self):
    maxi = self.numbers[0]
    for number in self.numbers:
        if number > maxi:
            maxi = number
    return maxi
