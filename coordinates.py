# measurements in mm
from math import sqrt

mmA = 74
mmC = 73
mmD = 82
mmE = 95
mmF = 105
mmG = 87
mmH = 52
mmI = 66
mmJ = 67
mmK = 84
mmL = 155
mmM = 165

# dimensions in mm
lenFinger = mmA
widFinger = 0.5 * min(mmH, mmI, mmJ)
dimPalmOne = 0.5 * mmC
dimPalmTwo = 0.5 * mmK
dimPalmThree = sqrt((0.8 * mmE)**2 - (mmC**2)) - dimPalmTwo
dimPalmFour = sqrt(mmF**2 - mmG**2)
dimPalmFive = mmG
widWrist = 0.5 * mmL

offTrap = 0.2 * mmE
widTrap = sqrt((-mmE + dimPalmTwo + dimPalmOne + dimPalmThree) * 
                  (mmE - dimPalmTwo + dimPalmOne + dimPalmThree) * 
                  (mmE - dimPalmTwo - dimPalmOne + dimPalmThree) * 
                  (mmE - dimPalmTwo + dimPalmOne - dimPalmThree)) / (2 * abs(mmE - dimPalmTwo))
#heron's formula
lenPalm = mmE
widRect = widFinger + sqrt(dimPalmFour**2 - offTrap**2)
widPalm = widTrap + widRect
lenHand = mmA + mmE

print("Sanity Check: \n\t Palm Length: ", lenPalm,
      " mm \n\t Rectangle Width: ", widRect,
      "mm \n\t Trapezoid Width: ", widTrap,
      " mm \n\t Palm Width: ", round(widPalm, 4), 
      " mm \n\t Hand Length: ", lenHand, " mm")

#dimensions in chips
cLenFinger = round(lenFinger * 0.6667)
cWidFinger = round(widFinger * 0.75)
cDimPalmOne = round(dimPalmOne * 0.6111)
cDimPalmTwo = round(dimPalmTwo * 0.9655)
cDimPalmThree = round(dimPalmThree * 0.5833)
cDimPalmFour = round(dimPalmFour * 0.8125)
cDimPalmFive = round(dimPalmFive * 0.7857)
cWidWrist = round(widWrist * 0.75)
cLenWrist = 26

cOffTrap = round(offTrap * 0.6667)
cWidTrap = round(widTrap * 0.75)
cLenPalm = round(lenPalm * 0.6667)
cWidRect = round(widRect * 0.75)
cWidPalm = round(widPalm * 0.75)
cLenHand = round(lenHand * 0.6667)

print("\n\nSanity Check 2: \n\t Palm Length: ", cLenPalm, 
      " chips \n\t Palm Width: ", cWidPalm, 
      " chips \n\t Hand Length: ", cLenHand, " chips")

#coordinates of chips
print("\n\nFinger Coordinates:")
print("\tTop Left Corner: (", cWidTrap, ", 0 )")
print("\tTop Right Corner: (", (cWidTrap + cWidFinger), ", 0 )")
print("\tBottom Left Corner: (", cWidTrap, ", ", cLenFinger, ") ")
print("\tBottom Right Corner: (", (cWidTrap + cWidFinger), ", ", cLenFinger, ") ")

v = round(sqrt(cDimPalmThree**2 - cWidTrap**2))
u = cLenPalm - cDimPalmTwo - v

print("\n\nPalm Coordinates:")
print("\t Point A: (", cWidTrap, ", ", cLenHand, ") ")
print("\t Point B: ( 0,", (cLenHand - v), " )")
print("\t Point C: ( 0 , ", (cLenFinger + cOffTrap + u), ") ")
print("\t Point D: (", cOffTrap, ", ", (cLenFinger + cOffTrap), ") ")
print("\t Point G: (", cWidPalm, ", ", (cLenFinger + cOffTrap), ") ")
print("\t Point H: (", round(cWidPalm - sqrt(cDimPalmFive**2 - (0.8 * cLenPalm)**2)), ", ", cLenHand, ") ")
print("\t Point I: (", cWidPalm, ", ", cLenFinger, ") ")
print("\t Point J: (", cWidPalm, ", ", cLenHand, ") ")

print("\n\nWrist Coordinates:")
print("\tTop Left Corner: (", cWidTrap, ", 0 )")
print("\tTop Right Corner: (", (cWidTrap + cWidWrist), ", 0 )")
print("\tBottom Left Corner: (", cWidTrap, ", ", (cLenHand + cLenWrist), ") ")
print("\tBottom Right Corner: (", (cWidTrap + cWidWrist), ", ", (cLenHand + cLenWrist), ") ")