from yodas import Menu, Yoda
import os


def choosePhone():
    jsons = []
    dataDir = config.contents()["phoneInfoDir"]
    for file in os.listdir(dataDir):
        if file.endswith(".txt"):
            jsons.append(file)
    print(jsons)


def calculateProfits():
    dataDir = config.contents()["phoneInfoDir"]
    name = dataDir + input("Input the phone model: ")
    phone = Yoda(name, ["sellPrice", "pricePhone", "priceBattery", "priceScreen", "priceChassis", "priceOther"])
    contents = phone.contents()
    losses = float(contents["pricePhone"]) + \
             float(contents["priceBattery"]) + \
             float(contents["priceScreen"]) + \
             float(contents["priceChassis"]) + \
             float(contents["priceOther"])
    profit = float(contents["sellPrice"]) - losses
    print("\n\tCost: €{0}\n\tSell: €{1}\n\tProfit: €{2}\n".format(losses,
                                                                  float(contents["pricePhone"]),
                                                                  profit))


def calculateBid():
    print("Hello 2")


def main():
    # Make sure the data dir finishes '/'
    dataDir = config.contents()["phoneInfoDir"]
    if not dataDir.endswith("/"):
        contents = config.contents()
        contents["phoneInfoDir"] = dataDir + "/"
        config.write(contents)

    # Start menu
    menu = Menu([exit, calculateProfits, calculateBid])
    while True:
        menu.select()


if __name__ == '__main__':
    # create config
    config = Yoda("config.json", ["phoneInfoDir"])
    main()
