print('WELCOME TO CHILDRENS VENDING MACHINE!')
def main_menu():
    print("1.CHOCALATES\n2.JUICES\n3.SNACKS\n4.BISCUITS\n5.ICE CREAMS")
    choice=int(input("Enter choice:"))
    if choice==1:

            a = {'item': 'DAIRY MILK', 'price': 40, 'stock': 100}
            b = {'item': 'KITKAT', 'price': 20, 'stock': 30}
            c = {'item': 'SNIKERS', 'price': 30, 'stock': 70}
            d = {'item': 'MILKYBAR', 'price': 10, 'stock': 10}
            e = {'item': 'FIVE STAR', 'price': 40, 'stock': 80}
            items = [a, b, c, d, e]


            print('\t\t\t\tWELCOME TO CHOCALATE SECTION')

            # show items, prices
            def show(items):
                print('\nitems available \n***************')
                print("NAME\t\tPRICE")

                for item in items:
                    if item.get('stock') == 0:
                        items.remove(item)
                for item in items:
                    print(item.get('item'), item.get('price'))

                print('***************\n')

            # have user choose item
            while True:

                show(items)
                selected = input('Select CHOCALATE: ')
                money = int(input("Insert amount:"))
                for item in items:
                    if selected == item.get('item'):
                        selected = item
                        price = selected.get('price')
                        if (money < price):
                            print("Given amount insufficient...\nPlease enter sufficient balance")
                        else:
                            print('you got ' + selected.get('item'))
                            selected['stock'] -= 1
                            money-= price
                            print('cash remaining: ' + str(money))
                            print('Take out Remaining cash')



                break
    if choice==2:
        a = {'item': 'SPIRIT', 'price': 90, 'stock': 100}
        b = {'item': 'APPLE JUICE', 'price': 70, 'stock': 30}
        c = {'item': 'FANTA', 'price': 50, 'stock': 70}
        d = {'item': 'PEPSI', 'price': 30, 'stock': 10}
        e = {'item': 'COCA COLA', 'price': 50, 'stock': 80}
        items = [a, b, c, d, e]

        print('\t\t\t\tWELCOME TO JUICE SECTION')

        # show items, prices
        def show(items):
            print('\nItems available \n***************')
            print("NAME\t\tPRICE")

            for item in items:
                if item.get('stock') == 0:
                    items.remove(item)
            for item in items:
                print(item.get('item'), item.get('price'))

            print('***************\n')

        # have user choose item
        while True:

            show(items)
            selected = input('  Choose Your Favourite Drink: ')
            money = int(input("Insert amount:"))
            for item in items:
                if selected == item.get('item'):
                    selected = item
                    price = selected.get('price')
                    if (money < price):
                        print("Given amount insufficient...\nPlease enter sufficient balance")
                    else:
                        print('you got ' + selected.get('item'))
                        selected['stock'] -= 1
                        money -= price
                        print('cash remaining: ' + str(money))
                        print('Take out Remaining cash')

            break
    if choice==3:
        a = {'item': 'SUN CHIPS', 'price': 100, 'stock': 100}
        b = {'item': 'CHOCOS', 'price': 50, 'stock': 30}
        c = {'item': 'CHEEZ-ITS', 'price': 125, 'stock': 70}
        d = {'item': 'POP-TARTS', 'price': 250, 'stock': 10}
        e = {'item': 'PLANTERS TRAIL MIX', 'price': 285, 'stock': 80}
        items = [a, b, c, d, e]

        print('\t\t\t\tWELCOME TO SNACKS SECTION')

        # show items, prices
        def show(items):
            print('\nitems available \n***************')
            print("NAME\t\tPRICE")

            for item in items:
                if item.get('stock') == 0:
                    items.remove(item)
            for item in items:
                print(item.get('item'), item.get('price'))

            print('***************\n')

        # have user choose item
        while True:

            show(items)
            selected = input('Select SNACKS : ')
            money = int(input("Insert amount:"))
            for item in items:
                if selected == item.get('item'):
                    selected = item
                    price = selected.get('price')
                    if (money < price):
                        print("Given amount insufficient...\nPlease enter sufficient balance")
                    else:
                        print('you got ' + selected.get('item'))
                        selected['stock'] -= 1
                        money -= price
                        print('cash remaining: ' + str(money))
                        print('Take out Remaining cash')

            break
    if choice==4:
        a = {'item': 'MILK BIKIS', 'price':50, 'stock': 100}
        b = {'item': 'GOOD DAY', 'price': 20, 'stock': 30}
        c = {'item': 'MARIE GOLD', 'price': 30, 'stock': 70}
        d = {'item': 'TREAT', 'price': 10, 'stock': 10}
        e = {'item': 'DARK FANTASY', 'price': 150, 'stock': 80}
        items = [a, b, c, d, e]

        print('\t\t\t\tWELCOME TO BISCUIT SECTION')

        # show items, prices
        def show(items):
            print('\nitems available \n***************')
            print("NAME\t\tPRICE")

            for item in items:
                if item.get('stock') == 0:
                    items.remove(item)
            for item in items:
                print(item.get('item'), item.get('price'))

            print('***************\n')

        # have user choose item
        while True:

            show(items)
            selected = input('Select BISCUIT Name: ')
            money = int(input("Insert amount:"))
            for item in items:
                if selected == item.get('item'):
                    selected = item
                    price = selected.get('price')
                    if (money < price):
                        print("Given amount insufficient...\nPlease enter sufficient balance")
                    else:
                        print('you got ' + selected.get('item'))
                        selected['stock'] -= 1
                        money -= price
                        print('cash remaining: ' + str(money))
                        print('Take out Remaining cash')

            break
    if choice==5:
        a = {'item': 'VENILLA', 'price': 150, 'stock': 100}
        b = {'item': 'STRAWBERRY', 'price': 120, 'stock': 30}
        c = {'item': 'CHOCALATE', 'price': 200, 'stock': 70}
        d = {'item': 'MOOSE TRACKS', 'price': 300, 'stock': 10}
        e = {'item': 'BUTTERED PECAN', 'price': 250, 'stock': 80}
        items = [a, b, c, d, e]

        print('\t\t\t\tWELCOME TO ICE-CREAM SECTION')

        # show items, prices
        def show(items):
            print('\nitems available \n***************')
            print("NAME\t\tPRICE")

            for item in items:
                if item.get('stock') == 0:
                    items.remove(item)
            for item in items:
                print(item.get('item'), item.get('price'))

            print('***************\n')

        # have user choose item
        while True:

            show(items)
            selected = input('Select ICE-CREAM Flavour: ')
            money = int(input("Insert amount:"))
            for item in items:
                if selected == item.get('item'):
                    selected = item
                    price = selected.get('price')
                    if (money < price):
                        print("Given amount insufficient...\nPlease enter sufficient balance")
                    else:
                        print('you got ' + selected.get('item'))
                        selected['stock'] -= 1
                        money -= price
                        print('cash remaining: ' + str(money))
                        print('Take out Remaining cash')

            break



a = input('DO YOU WANT TO BUY SOMETHING ? (y/n): ')
if a == 'n':
    print("Thank you for visiting our service..."
          )


else:
    main_menu()
