def decor(x):
    print('before')
    print(x)
    print('after')
decor('makanan')



# def decor(func):
#     def wrap():
#         print('before')
#         func()
#         print('after')
#     return wrap
# @decor
# def nama():
#     print('silvio')
# nama()

# dapat disimpulkan nama() pada def nama() =  func()


def decor(func):
    def wrap():
        print('before')
        func()
        print('after')
    return wrap
@decor
def nama():
    print('silvio')
nama()



def decora(func):
    def wrapp(x):
        print('before')
        hasil = func(x)
        print('after')
        return hasil
    return wrapp

@decora
def namaa(x):
    print(f'Halooo {x}')
namaa('silvio')

@decora
def makan(x):
    print(f'{x} enak')
makan('nasi goreng')





