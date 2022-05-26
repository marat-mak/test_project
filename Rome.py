num = int(input('Введите арабское число:\n'))
mills = num//1000
num = num%1000
sotni = num//100
num = num%100
tens = num//10
edin = num%10
if 0<=mills<=3:
    digit_1 = 'M' * mills
if 0<=sotni<=3:
    digit_2 = 'C' * sotni
elif sotni == 4:
    digit_2 = 'CD'
elif 5<=sotni<=8:
    digit_2 = 'D' + 'C' * (sotni-5)
else:
    digit_2 = 'CM'
if 0<=tens<=3:
    digit_3 = 'X' * tens
elif tens == 4:
    digit_3 = 'XL'
elif 5<=tens<=8:
    digit_3 = 'L' + 'X' * (tens-5)
else:
    digit_3 = 'XC'
if 0<=edin<=3:
    digit_4 = 'I' * edin
elif edin == 4:
    digit_4 = 'IV'
elif 5<=edin<=8:
    digit_4 = 'V' + 'I' * (edin-5)
else:
    digit_4 = 'IX'
print(digit_1+digit_2+digit_3+digit_4)