class MyClass:
    def __init__(self):
        self.public_var = 42       # Variabel publik
        self._protected_var = 24   # Variabel dilindungi (protected)
        self.__private_var = 12    # Variabel pribadi (private)

    def private(self):
        return self.__private_var

    def public_method(self):
        print("Ini adalah method publik")

    def _protected_method(self):
        print("Ini adalah method dilindungi")

    def __private_method(self):
        print("Ini adalah method pribadi")


# Membuat instance dari kelas MyClass
obj = MyClass()

# Mengakses variabel
print(obj.public_var)          # Output: 42
print(obj._protected_var)      # Output: 24
print(obj.private())     # Error: AttributeError

# Memanggil method
obj.public_method()            # Output: Ini adalah method publik
obj._protected_method()        # Output: Ini adalah method dilindungi
# obj.__private_method()      # Error: AttributeError

# Namun, variabel atau method dengan __ dapat diakses secara tidak langsung
print(obj._MyClass__private_var)   # Output: 12
obj._MyClass__private_method()     # Output: Ini adalah method pribadi
