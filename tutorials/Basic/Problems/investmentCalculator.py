'''
1. SIP calculator
2. Lumpsum calculator
'''

i = 0.12

def SIPCalculator(tenure, sipAmount):
    returns = sipAmount * (((1 + i) * (tenure - 1)) / ((1 + i) * i) )
    print(returns)

def LumpsumCalculator(tenure, lumpsumAmount):
    pass

investmentType = int(input("Choose investment type\n1. SIP\n2. Lumpsum\nchoice: "))
tenure = int(input("Number of years: "))

if investmentType == 1:
    sipAmount = float(input("SIP Amount: "))
    SIPCalculator(tenure, sipAmount)

else:
    lumpsumAmount = float(input("Lumpsum Amount: "))
    LumpsumCalculator(tenure, lumpsumAmount)

