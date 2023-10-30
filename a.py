#klases veidošanas specifika
class RUDENS:

    def _init_(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums
    def araa(self):
        print(self.vards, self.vecums)

#tiek izveidots objekts

p = RUDENS()

p.araa()

