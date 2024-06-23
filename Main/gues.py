import random

class TahminOyunu:
    def __init__(self, s1=0, s2=100):
        self.a = random.randint(s1, s2)
        self.b = 8
        self.s1 = s1
        self.s2 = s2

    def reset(self):
        self.a = random.randint(self.s1, self.s2)
        self.b = 8

    def tahmin_et(self, kullanici_tahmini):
        if self.b <= 0:
            return "Hakkınız kalmadı. Doğru sayı {} idi.".format(self.a), False
        
        try:
            kullanici_tahmini = int(kullanici_tahmini)
        except ValueError:
            return "Sayı girmeniz lazım", True

        self.b -= 1
        if kullanici_tahmini == self.a:
            return "Doğru tahmin! Tebrikler.", False
        elif kullanici_tahmini < self.a:
            if self.b > 0:
                return "Daha büyük bir tahminde bulunun. {} hakkınız kaldı".format(self.b), True
            else:
                return "Hakkınız kalmadı. Doğru sayı {} idi.".format(self.a), False
        else:
            if self.b > 0:
                return "Daha küçük bir tahminde bulunun. {} hakkınız kaldı".format(self.b), True
            else:
                return "Hakkınız kalmadı. Doğru sayı {} idi.".format(self.a), False
