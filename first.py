def new_func(*args, keyword):
    print("Ваши числа:", args)
    return print(f"Ваши числа в {keyword} степени:", [number**keyword for number in args])

print(new_func(2, 4, 6, 8, 10, 12, keyword=4))