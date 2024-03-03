my_list = [1, 2, 3]
my_list.append(4)  # Menambahkan elemen 4 pada akhir daftar
print(my_list)  # Output: [1, 2, 3, 4]

another_list = [5, 6, 7]
my_list.extend(another_list)  # Menambahkan elemen-elemen dari another_list ke dalam my_list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]



my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # Menambahkan pasangan kunci-nilai baru
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

another_dict = {'d': 4, 'e': 5}
my_dict.update(another_dict)  # Menambahkan pasangan kunci-nilai dari another_dict ke dalam my_dict
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}



my_set = {1, 2, 3}
my_set.add(4)  # Menambahkan elemen 4 ke dalam set
print(my_set)  # Output: {1, 2, 3, 4}

another_set = {5, 6, 7}
my_set.update(another_set)  # Menambahkan elemen-elemen dari another_set ke dalam my_set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
