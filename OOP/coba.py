def decorator(func):
    def wrapper(*args, **kwargs):
        print("Sebelum eksekusi fungsi")
        result = func(*args, **kwargs)
        print("Setelah eksekusi fungsi")
        return result
    return wrapper

@decorator
def contoh_fungsi(x):
    y = [x, 10, 7, x, 9]
    return y

print(contoh_fungsi(5))
print()


def decorator(func):
    def wrapper(x):
        print("Sebelum eksekusi fungsi")
        result = func(x)
        print("Setelah eksekusi fungsi")
        return result
    return wrapper

@decorator
def contoh_fungsi(x):
    y = [x, 10, 7, x, 9]
    return y

print(contoh_fungsi(5))
