sandwich = input("Enter sandwich type (Chicken / Beef / Veg): ")

match sandwich:
    case "Chicken":
        print("Price: 120")
    case "Beef":
        print("Price: 150")
    case "Veg":
        print("Price: 100")
    case _:
        print("Sorry, this sandwich is not available in the menu")
