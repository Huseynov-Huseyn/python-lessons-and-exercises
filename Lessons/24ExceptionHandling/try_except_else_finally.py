def divide():
    try:
        num = int(input("Number:"))
        result = 100 / num
    except ValueError:
        print("Wrong input type!")
    except ZeroDivisionError:
        print("Cannot divide by 0")

    # Only work no except situations
    else:
        print(f"Result: {result}")
    # Always work even have return 
    finally:
        print("End")
