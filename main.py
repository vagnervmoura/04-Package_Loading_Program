# 04 - Package Loading Program

list_n_items = []
list_n_package = []
package = 0
item = 0
n_item = 0
min = 1
max = 10

n_itens_to_ship = int(input("Enter the number of items to ship: "))
while n_itens_to_ship > n_item:
    try:
        item_w = int(input("Enter the weight of item " + str(n_item+1) + ": "))
        if item_w == 0:
            break
        elif min <= item_w <= max:
            if package + item_w <= 20:
                package = package + item_w
                print("Package Weight: ", package)
                n_item += 1
            else:
                print("Lets to pack next package")
        elif item_w > max:
            print("Item to heavier than 10kg, please remove:", item_w - 10,"from your Item.")
    except ValueError:
        print("Sorry, but you have input a wrong weight, please let's try again with an valid weight.")
