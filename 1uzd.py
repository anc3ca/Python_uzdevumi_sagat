"""
Uzrakstiet programmu definējot klasi,
lai veselu skaitli pārveidotu par romiešu ciparu.

"""

class AAA:
    def _init_(self):
        self.roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
    def uz_roman(self, num):
        result = "" # definē tukšu virkni!! <3
        for value, numeral in sorted(self.roman_numerals.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result+=numeral
                num = value
        return result
    


# piemērs
skaitlis = 1984
convert = AAA()
roman_nueral = convert.to_roman(skaitlis) # convertēt tas ir objekts, objektam es izsaucu metodi, self ir parametrus, skaitlis ir mainīgais parametrs
print(f"{skaitlis} romiešu cipars ir {roman_nueral}") #formatē un  uzraksta tads sk romiesu ciparos ir taads