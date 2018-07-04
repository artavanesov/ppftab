# Car Salesman

base_price = int(input("Please enter the base price of vehicle: "))

tax = base_price / 100 * 15
license = base_price / 100 * 10
dealer_prep = 150
destination_charge = 200

print("Base price: ", base_price)

print("\nTax: ", tax)
print("License: ", license)
print("Dealer prep: ", dealer_prep)
print("Destination charge: ", destination_charge)

print("\n\nTotal: ", base_price + tax + license + dealer_prep + destination_charge)

input("\nPress the Enter key to exit.")
