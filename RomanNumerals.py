class RomanNumeralConverter:

    def __init__(self):

        self.FiveK =  (u'\u024E') # symbol for 5,000
        self.TenK = (u'\u03C7')  # symbol for 10,000
        self.FiftyK = (u'\u013B')  # symbol for 50,000

        self.keys = [self.FiftyK,self.TenK,self.FiveK,'M','D','C','L','X','V','I']
        self.values = [50000,10000,5000,1000,500,100,50,10,5,1]

    def CheckEdgeCase(self,num):
        idx = 0
        while idx < len(self.values): #Loop through our values comparing each to our current index
            for val in enumerate(self.values):
                #Check if our current index - each value is equal to the paramater we passed in.
                if(num == ( self.values[idx] - val[1] ) and num != val[1] ):
                    result = [ self.keys[val[0]] , self.keys[idx] ] #Return the difference between the index and value, along with the current index
                    return result                      #ie. 90 is 100-10 (both in our values arr) so return [10,100] or (XC)
            idx += 1 
        return False

    def ConvertRomanNumerals(self,inputNum):
        romanNumeralString = ""
        for k in enumerate(self.keys): #loop through our keys until we have no remainder

            if inputNum == 0: #if we have no remainder exit early and return the romanNumeralString
                return romanNumeralString

            #otherwise check for edge cases
            edge = self.CheckEdgeCase(inputNum) 
            #we ran into an edge cases, conactinate the string and return the converted Roman Numeral
            if( edge != False):
                romanNumeralString += edge[0] + edge[1]
                return romanNumeralString
            else: #we found no edge cases, get our remainder & count occurnces of RomanNumeral
                for val in enumerate(self.values):
                    if(inputNum >= val[1]): 
                        remainder = inputNum % val[1]
                        inputNumCount = inputNum // val[1] #number of occurences ie. (30 is X 3 times)
                        for i in range (0,inputNumCount):
                            romanNumeralString += self.keys[val[0]]
                        inputNum = remainder
                        
        return romanNumeralString #return the RomanNumerial for the provided digit

    def ConvertNumber(self,numberToConvert):
        return self.ExplodeInt(numberToConvert)

    #Explode the number paramater into a string, then find the appropriate value for each digit.
    #ie. 999 = 900, 90, 9 
    def ExplodeInt(self,number):
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
            for z in range(0,zeros): 
                ExtractedDigit *= 10

            #for each Exploded digit with appropriate zeros, convert it to a RomanNumerial
            R = self.ConvertRomanNumerals(ExtractedDigit) 
            romanNumeral += R       

        return romanNumeral

c = RomanNumeralConverter()
x = 0
while x == 0:
    i = input("Enter a whole number to convert...")
    if "exit" in i or "clear" in i:
        print("bye!")
        break;
    print( c.ConvertNumber(i) )


