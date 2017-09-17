# CTI-110
# M2HW2_Tip Tax Total
# Stoker Winston
# 17 Sept 2017
# Tip, Tax and Total

#foodcharge
foodCharge =float(input ('Please enter the charge of food: '))

#Tip
tip = 0.18 * foodCharge

#salesTax
salesTax= 0.07 * foodCharge

#total
total = foodCharge + tip + salesTax

print ('food charge: $' + format ( foodCharge, ',.2f' ))

print ('tip: $' + format (tip, ',.2f'))

print ('salestax: $' + format (salesTax, ',.2f'))

print ('total: $ ' + format (total, ',.2f'))

