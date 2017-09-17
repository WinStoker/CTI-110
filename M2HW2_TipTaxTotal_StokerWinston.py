# CTI-110
# M2HW2_Tip Tax Total
# Stoker Winston
# 17 Sept 2017
# Tip, Tax and Total

#foodcharge
food_charge =float(input ('Please enter the charge of food: '))

#Tip
tip = 0.18 * food_charge

#salesTax
sales_tax= 0.07 * food_charge

#total
total = food_charge + tip + sales_tax

print ('Food Charge: $' + format ( food_charge, ',.2f' ))

print ('Tip: $' + format (tip, ',.2f'))

print ('Sales Tax: $' + format (sales_tax, ',.2f'))

print ('Total: $ ' + format (total, ',.2f'))

