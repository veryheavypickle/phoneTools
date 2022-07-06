# Program calculates the maximum bidding price

name = input("Input the name and storage of the phone: ")
minProfit = float(input("Input the minimum profit you would like: €"))
sellPrice = float(input("Input the minimum sell price of this phone: €"))
print("Input the price of the adhesive, screen, battery and chassis for this device")
repairCost = float(input("also include shipping cost for replacement parts: €"))
shippingCost = float(input("Input the price of shipping for device: €"))

maxBid = sellPrice - repairCost - minProfit - shippingCost
print("")
print("Max bidding price: €{0} + €{1}".format(round(maxBid, 2), shippingCost))
print("Max bidding price: £{0} + £{1}".format(round(maxBid * 0.88, 2), round(shippingCost * 0.88, 2)))
print("Max bidding price: ${0} + ${1}".format(round(maxBid * 1.23, 2), round(shippingCost * 1.23, 2)))
print("")
print("Total: €{0}".format(round(maxBid + shippingCost, 2)))
