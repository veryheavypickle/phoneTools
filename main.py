def calculateBid():
    specificQuestions = False
    # currency: value in euros
    exchangeRate = {"€": 1.00,
                    "£": 1.17}

    costToRepair = 0
    if specificQuestions:
        itemList = ["battery", "screen", "chassis"]
        for item in itemList:
            costToRepair += getValidatedInput("What is the price of a new {0}?: €".format(item))
        costToRepair += getValidatedInput("What is the shipping price: €")
    else:
        costToRepair = getValidatedInput("What is the total cost to repair (incl shipping)?: €")

    salePrice = getValidatedInput("What is the sale price: €")
    desiredProfit = getValidatedInput("What is your desired profit: €")

    maxPrice = salePrice - (desiredProfit + costToRepair)
    vat = 1.21

    print("\nFor a profit of €{0}".format(round(desiredProfit)))
    print("VAT incl.\tVAT excl.")
    for currency in exchangeRate:
        localCurrency = maxPrice / exchangeRate[currency]
        localCurrencyVat = round(localCurrency * (1 / vat))
        price = "{0} {1}\t\t{0} {2}".format(currency, round(localCurrency), localCurrencyVat)
        print(price)


def calculateProfit():
    losses = getValidatedInput("What is the final sale price including shipping?: €")
    losses += getValidatedInput("What is the total cost to repair?: €")
    salePrice = getValidatedInput("What is the estimated sale price?: €")
    print("\nYour profit is €{0}".format(round(salePrice - losses, 2)))


def getValidatedInput(question):
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("That doesn't look like a good number")


def menu(options):
    print("")
    print("=" * 50)
    print("0: Exit")
    for i in range(len(options)):
        print("{0}: {1}".format(i + 1, options[i]))
    chosenOption = int(getValidatedInput("Choose an option: "))
    if chosenOption == 0:
        exit()
    print("=" * 50)
    print("")
    return chosenOption - 1


def main():
    menuOptions = ["Calculate bid price", "Calculate profit"]
    chosenOption = menu(menuOptions)
    if chosenOption == 0:
        calculateBid()
    elif chosenOption == 1:
        calculateProfit()


if __name__ == '__main__':
    main()
