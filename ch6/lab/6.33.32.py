# CS-003 - 6.33.32
# 7/18/2024
# Zoraida Rodriguez
# Timothy Sanders
#
# Problem Statement
# A pet shop wants to give a discount to its clients if they buy one or more pets and at least five other items.
# The discount is equal to 20 percent of the cost of the other items, but not the pets.
import textwrap

## This function will validate that the sales price entered is a valid price which
## contains only numeric characters and the `.` character. Prices below zero will be considered invalid
#  @param inputPrice: str - the price string that was entered by the user of the application
#  @return bool - indicates whether the input price is valid or not
def validateInputPrice(inputPrice: str) -> bool:
    priceValid = False
    if inputPrice.replace('.','').isdigit() or inputPrice == "-1":
        priceValid = True
    return priceValid


## This function will validate that the string the user enters in response to the
## “Is this a pet? (Y/N): “ prompt is a ‘Y’ or an ‘N’
#  @param inputPet: str - the response string that was entered by the user of the application
#  @returns bool - indicates whether or not the input string is valid or not
def validateInputPet(inputPet: str) -> bool:
    petValid = False
    if inputPet.upper() == "Y" or inputPet.upper() == "N":
        petValid = True
    return petValid


## The discount() function will accept a single list of items to be sold and will calculate the original sale
## price and the discount sale price of non-pet items, provided there are more than five non-pet items in the sale
##
## The discount that will be applied to sales of five or more non-pet items will be 20% off
##
## The number of items in the sale will be calculated from the length of the input list
#  @param saleItems: tuple[float, bool] - a list of tuples, with each tuple containing a floating point price and a
#           boolean indicating whether this particular price is for a pet
#  @return tuple[float, float] - A tuple containing the total price and the total discounted price
def discount(saleItems: list[tuple[float, bool]]) -> tuple[float, float]:
    petSaleCount = 0
    nonPetSaleCount = 0
    totalSales = 0
    totalPetSales = 0
    totalNonPetSales = 0
    # Iterate through our list of sold items
    for item in saleItems:
        salePrice = item[0]
        totalSales += salePrice
        # Process sales that are of pets
        if item[1] is True:
            petSaleCount += 1
            totalPetSales += salePrice
        # Process sales of non-pet items
        else:
            nonPetSaleCount += 1
            totalNonPetSales += salePrice
    # If the sale meets the criteria of at least one pet and
    # at least five other non-pet items, discount non-pet
    # items by 20%
    if petSaleCount >= 1 and nonPetSaleCount >= 5:
        return totalSales, totalPetSales + (totalNonPetSales * 0.8)
    # If the sale does not meet the criteria, return the total sales amount
    else:
        return totalSales, totalSales

## Prints a message that summarizes sales prices of the items entered. The total, pre-discount sales price
## will be shown, along with the discounted sale price, if applicable
#  @param finalPrices: tuple[float, float] - A tuple containing the total sales price and the discounted price
#  @return None
def printSaleMessage(finalPrices: tuple[float, float]) -> None:
    if finalPrices[0] == 0:
        totalPrice = "N/A"
    else:
        totalPrice = "$%.2f" % finalPrices[0]
    if finalPrices[1] == finalPrices[0]:
        discountedPrice = "N/A"
    else:
        discountedPrice = "$%.2f" % finalPrices[1]
    salesMessage = """
    The total price is: %s
    The discounted price is: %s
                  Woof!
             __  /
       (___()'`;
       /,    /`
       \\\\---\\\\
    """ % (totalPrice, discountedPrice)
    print(textwrap.dedent(salesMessage))


def main():
    saleItems = []
    userPrice = 0
    print("Welcome to Paws and Claws Emporium!")
    while userPrice != "-1":
        inputPrice = input("Please enter the price of the current item (enter '-1' to exit): ")
        if inputPrice == "-1":
            break
        validPrice = False
        while not validPrice:
            validPrice = validateInputPrice(inputPrice)
            if not validPrice:
                print("ERROR: The price entered, `%s`, contains invalid characters. Please enter only positive floating point numbers" % inputPrice)
                inputPrice = input("Please enter the price of the current item (enter '-1' to exit): ")
        inputPet = input("Is this a pet? (Y/N): ")
        validPet = False
        while not validPet:
            validPet = validateInputPet(inputPet)
            if not validPet:
                print("ERROR: The response entered `%s`, contains invalid characters. Please enter only Y or N" % inputPet)
                inputPet = input("Is this a pet? (Y/N): ")
        if inputPet.upper() == "Y":
            processedPet = True
        else:
            processedPet = False
        saleItems.append((float(inputPrice), processedPet))
    # If there have been items entered for the sales, calculate the discount
    if saleItems is True:
        calculatedPrices = discount(saleItems)
        printSaleMessage(calculatedPrices)
    # Otherwise print a closing message
    else:
        salesMessage = """
        No items were entered for sale!
                      Woof!
                 __  /
           (___()'`;
           /,    /`
           \\\\---\\\\
        """
        print(textwrap.dedent(salesMessage))


# UNIT TESTS
assert validateInputPrice("-1")
assert validateInputPrice("19.99")
assert validateInputPrice("tim") is False
assert validateInputPet("Y")
assert validateInputPet("N")
assert validateInputPet("y")
assert validateInputPet("n")
assert validateInputPet("yes") is False

if __name__ == "__main__":
    main()
