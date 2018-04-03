FiveK =  (u'\u024E') # symbol for 5,000
TenK = (u'\u03C7')  # symbol for 10,000
FiftyK = (u'\u013B')  # symbol for 50,000

keys = [FiftyK,TenK,FiveK,'M','D','C','L','X','V','I']
values = [50000,10000,5000,1000,500,100,50,10,5,1]

def CheckEdgeCase(num):
    idx = 0
    while idx < len(values): #Loop through our values comparing each to our current index
        for e in enumerate(values):
            #Check if our current index - each value is equal to the paramater we passed in.
            if(num == (values[idx] - e[1]) and num != e[1]):
                result = [ keys[e[0]], keys[idx] ] #Return the different between the index and value, along with the current index
                return result                      #ie. 90 is 100-10 (both in our values arr) so return [10,100]
        idx += 1 
    return False

def ConvertRomanNumerals(RM):
    RM_String = ""
    for key in enumerate(keys): #loop through our keys

        if RM == 0: #if we have no remainder exit early and return the RM_String
            return RM_String

        #otherwise check for edge cases
        edge = CheckEdgeCase(RM) 
        #we ran into an edge cases, conactinate the string and return
        if( edge != False):
            RM_String += edge[0] + edge[1]
            return RM_String
        else: #we found no edge cases, get our remainder and count how many times that RomanNumerial is divided evenly by our current value
            for val in enumerate(values):
                if(RM >= val[1]):
                    remainder = RM % val[1]
                    RM_Count = RM / val[1]
                    for RMC in range (0,RM_Count):
                        RM_String += keys[val[0]]
                    RM = remainder
                    
    return RM_String #return the RomanNumerial for the provided digit

#Explode the number paramater into a string, then find the appropriate value for each digit.
#ie. 999 = 900, 90, 9 
def ExplodeInt(number):
    RomanNumeral = ""

    numStr = str(number)

    for digit in enumerate(numStr): #loop through our exploded digits

        if(int(digit[1]) == 0): #skip over any digit that is 0
            continue

        #find how many zeros follow each exploded digit
        z = len(numStr)-1 
        zeros = z - digit[0] 
        ExtractedDigit = int(digit[1])

        #loop through our 'zeros' and multiple our digit by 10 for each zero,
        #the first 9 in 999 becocmes 900, the second 90, etc
        for zero in range(0,zeros): 
            ExtractedDigit *= 10
            if zeros < 1:
                ExtractedDigit -=1

        #for each Exploded digit with appropriate zeros, convert it to a RomanNumerial
        R = ConvertRomanNumerals(ExtractedDigit) 
        RomanNumeral += R       

    return RomanNumeral

print ExplodeInt(5231)

