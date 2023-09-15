# 04 - Package Loading Program

list_n_package = []
package = 0
n_package = 1
item_w = 0
n_item = 0
min = 1
max = 10
package_kg_total = 0
non_optimal_package = 20
min_unused_n_package = None
amount_unused_package = None

def goto(linenum):
    global line
    line = linenum

line = 1

n_itens_to_ship = int(input("Enter the number of items to ship: "))

while n_itens_to_ship > n_item:
    try:
        item_w = float(input("Enter the weight of item " + str(n_item+1) + ": "))
        if item_w == 0:
            if n_package == 1 and package == 0:
                print("We do not have any Package to send.\n\n")
                exit()
            else:
                break
        elif min <= item_w <= max:
            if package + item_w <= 20:
                package = package + item_w
                print("Package {} is loaded with {}kg, total of {}kg is available to fill this package.\n\n".format(n_package, package, 20 - package))
                n_item += 1
                list_n_package.append(["N_Package:", n_package, "Package Kilo:", package, "N_Item:", n_item, "Item Kilo:", item_w])
                package_kg_total = package_kg_total + item_w
            elif n_itens_to_ship > n_item:
                print("Package {}, its in the maximun load. Cannot add this item with {}kg to this package, sending this Item to the next Package.".format(n_package, item_w))
                if package < 20 and package < non_optimal_package:
                    min_unused_n_package = n_package
                    amount_unused_package = 20 - package
                    non_optimal_package = package

                package = 0
                n_package += 1
                n_item += 1
                package = package + item_w
                list_n_package.append(["N_Package:", n_package, "Package Kilo:", package, "N_Item:", n_item, "Item Kilo:", item_w])
                package_kg_total = package_kg_total + item_w 
        elif item_w > max:
            print("Item to heavier than 10kg, please remove: {}kg from your Item.".format(item_w - 10))
    except ValueError:
        print("Sorry, but you have input a wrong weight, please let's try again with an valid weight.")
    line == 100
print("=" *100)

print(n_package, "Packages to send.")
print(package_kg_total, "Kilos total to send.") 
print(n_package * 20 - package_kg_total, "Total unused of capacity due a non-optimal packaging.")

if package < 20 and package < non_optimal_package:
    min_unused_n_package = n_package
    amount_unused_package = 20 - package
    non_optimal_package = package
    print("Package Number:", min_unused_n_package, "had the most 'unused' capacity, with an amount of", amount_unused_package, "kg unused.")
else:
    print("Package Number:", min_unused_n_package, "had the most 'unused' capacity, with an amount of", amount_unused_package, "kg unused.")
                  
print("=" *100)  