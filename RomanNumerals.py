FiveK =  (u'\u024E') # symbol for 5,000
TenK = (u'\u03C7')  # symbol for 10,000
FiftyK = (u'\u013B')  # symbol for 50,000

keys = [FiftyK,TenK,FiveK,'M','D','C','L','X','V','I']
values = [50000,10000,5000,1000,500,100,50,10,5,1]

def CheckEdgeCase(num):
    idx = 0
    while idx < len(values): #Loop through our values comparing each to our current index
        for val in enumerate(values):
            #Check if our current index - each value is equal to the paramater we passed in.
            if(num == ( values[idx] - val[1] ) and num != val[1] ):
                result = [ keys[val[0]] , keys[idx] ] #Return the difference between the index and value, along with the current index
                return result                      #ie. 90 is 100-10 (both in our values arr) so return [10,100] or (XC)
        idx += 1 
    return False

def ConvertRomanNumerals(inputNum):
    romanNumeralString = ""
    for k in enumerate(keys): #loop through our keys until we have no remainder

        if inputNum == 0: #if we have no remainder exit early and return the romanNumeralString
            return romanNumeralString

        #otherwise check for edge cases
        edge = CheckEdgeCase(inputNum) 
        #we ran into an edge cases, conactinate the string and return the converted Roman Numeral
        if( edge != False):
            romanNumeralString += edge[0] + edge[1]
            return romanNumeralString
        else: #we found no edge cases, get our remainder & count occurnces of RomanNumeral
            for val in enumerate(values):
                if(inputNum >= val[1]): 
                    remainder = inputNum % val[1]
                    inputNumCount = inputNum // val[1] #number of occurences ie. (30 is X 3 times)
                    for i in range (0,inputNumCount):
                        romanNumeralString += keys[val[0]]
                    inputNum = remainder
                    
    return romanNumeralString #return the RomanNumerial for the provided digit

#Explode the number paramater into a string, then find the appropriate value for each digit.
#ie. 999 = 900, 90, 9 
def ExplodeInt(number):
    romanNumeral = ""
    numStr = str(number)

    for digit in enumerate(numStr): #loop through our exploded digits

        if(int(digit[1]) == 0): #skip over any digit that is 0
            continue

        #find how many zeros follow each exploded digit
        totalZeros = len(numStr)-1 
        zeros = totalZeros - digit[0] 
        ExtractedDigit = int(digit[1])

        #loop through our 'zeros' and multiple our digit by 10 for each zero,
        #the first 9 in 999 becocmes 900, the second 90, etc
        for zero in range(0,zeros): 
            ExtractedDigit *= 10

        #for each Exploded digit with appropriate zeros, convert it to a RomanNumerial
        R = ConvertRomanNumerals(ExtractedDigit) 
        romanNumeral += R       

    return romanNumeral

print(ExplodeInt(980))

