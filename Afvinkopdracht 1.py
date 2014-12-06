####################################################################
#Richard Jansen 1337 HAX code to determine aspertame levels in soda#
#with added function to calculate personal ADI value################
#Written on 14-11-2014###########################################
######################################################
gasp = int(input("hoeveelheid gram aspartaam: "))                   #Amount of aspartame in Gram
vol = int(input ("volume frisdrank in M3:  "))                      #Volume of soda in cubic meters
mol = gasp/294.30                                                   #calculation of Amount of mols of aspartame in the given weight
print ("hoeveelheid mol aspartaam: " + str(mol))                    #output of previous calculation
gvol = (gasp/vol)*1.5                                               #calculation to determine the amount of aspartame in one bottle of soda
print ("mg per 1.5 liter: " + str(gvol))                            #output of previous calculation
ADI = 2800 // gvol                                                  #calculation to determine the maximum amount of permitted bottles of soda
print ("maximaal aantal flessen volgens ADI waarde: " + str(ADI))   #output of previous calculation
naam = input("wat is uw naam? ")                                    #query of name
gewicht = int(input("wat is uw gewicht? "))                         #query of bodymass
pADI = 40*gewicht                                                   #calculation of maximum intake of aspartame per day in mg
print ("maximale inname per dag in mg/dag= " +str(pADI))            #output of previous calculation


