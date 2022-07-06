# Program calculates the profit from winning

name = input("Input the name and storage of the phone: ")
sellPrice = float(input("How much will you sell your {0}: €".format(name)))
refurb = float(input("Input the refurbish cost: €"))
shipping = float(input("Input the shipping price for the device: €"))
finalBid = float(input("Input the final bid price: €"))

profit = sellPrice - (refurb + shipping + finalBid)

print("")
print("Your profit will be €{0}".format(round(profit, 2)))
