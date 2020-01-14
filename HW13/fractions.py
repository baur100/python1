class Fraction:
    whole=0
    numerator=0
    denominator=0
    def print_fraction(self):
        print(f"Fraction is {self.whole} {self.numerator}/{self.denominator}")

    def add_whole(self, x):
        self.whole+=x
    def change_den(self, x):
        if not x:
            raise ZeroDivisionError("Denominator cannot be 0")
        self.denominator=x
    def add_fraction(self, new_num, new_den):
        if self.denominator==new_den:
            self.numerator+=new_num
        else:
            d=self.denominator*new_den
            self.numerator=self.numerator*new_den+new_num*self.denominator
            self.denominator=d
    def check_ProperFr(self):
        if self.isFraction():
            return self.numerator<self.denominator and not self.whole

    def isFraction(self):
        return not self.whole and self.numerator>=self.denominator