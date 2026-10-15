def main():
    print("Выберите категорию еды: напиток | суп | десерт")
    
    category = input("Введите желаемое блюдо: ")

    match category:
        case "напиток":
            print("чай | кофе | сок")
            item = input("Выберите напиток: ")
            
            match item:
                case "чай":
                    print("120 руб")
                case "кофе":
                    print("215 руб")
                case "сок":
                    print("683 руб")
                case _:
                    print("Надо выбрать что-то из перечисленного")

        case "суп":
            print("борщ | щи | суп-пюре")
            item = input("Выберите суп: ")
            
            match item:
                case "борщ":
                    print("634 руб.")
                case "щи":
                    print("578 руб.")
                case "суп-пюре":
                    print("64 руб")
                case _:
                    print("Надо выбрать что-то из перечисленного")

        case "десерт":
            print("торт | мороженое | фрукты")
            item = input("Выберите десерт: ")
            
            match item:
                case "торт":
                    print("2573 руб.")
                case "мороженое":
                    print("375 руб.")
                case "фрукты":
                    print("54 руб.")
                case _:
                    print("Надо выбрать что-то из перечисленного")

        case _:
            print("Такого нет")

if __name__ == "__main__":
    main()def main():
    print("Выберите категорию: напиток | суп | десерт")
    
    category = input("Введите желаемое блюдо: ")

    match category:
        case "напиток":
            print("чай | кофе | сок")
            item = input("Выберите напиток: ")
            
            match item:
                case "чай":
                    print("120 руб")
                case "кофе":
                    print("215 руб")
                case "сок":
                    print("683 руб")
                case _:
                    print("Надо выбрать что-то из перечисленного")

        case "суп":
            print("борщ | щи | суп-пюре")
            item = input("Выберите суп: ")
            
            match item:
                case "борщ":
                    print("634 руб.")
                case "щи":
                    print("578 руб.")
                case "суп-пюре":
                    print("64 руб")
                case _:
                    print("Надо выбрать что-то из перечисленного")

        case "десерт":
            print("торт | мороженое | фрукты")
            item = input("Выберите десерт: ")
            
            match item:
                case "торт":
                    print("2573 руб.")
                case "мороженое":
                    print("375 руб.")
                case "фрукты":
                    print("54 руб.")
                case _:
                    print("Надо выбрать что-то из перечисленного")

        case _:
            print("Такого нет")

if __name__ == "__main__":
    main()
