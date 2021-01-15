import string
import random 

class Robot:
    def __init__(self):
        self.name = self.generate_name()
    
    def generate_name(self):
        A_Z = list(string.ascii_uppercase)
        numbers = list(string.digits)
        rand_num = "".join(random.sample(numbers, 3))
        random_string = "".join(random.sample(A_Z, 2))
        self.name = f"{random_string}{rand_num}"
        return self.name

    def reset(self):
      self.name = ''