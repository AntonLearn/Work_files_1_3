import os

def create_cook_book(root_of_path, file_name, mode, coding_type, keys_of_ingredient):
    full_path_of_recipes_file = os.path.join(root_of_path, file_name)
    cooking_book = {}
    with open(full_path_of_recipes_file, mode, encoding=coding_type) as file_of_recipes:
        eof = False
        while not eof:
            name_recipe = file_of_recipes.readline().rstrip()
            if not name_recipe:
                eof = True
            else:
                list_of_ingredients = []
                for i_ingredient in range(int(file_of_recipes.readline().rstrip())):
                    list_of_ingredients.append(dict(zip(keys_of_ingredient, file_of_recipes.readline().rstrip().split(" | "))))
                cooking_book[name_recipe] = list_of_ingredients
                delimiter_str = file_of_recipes.readline()
    return cooking_book

def get_shop_list_by_dishes(dishes, person_count, keys_of_ingredient, cooking_book):
    dict_for_shoping = {}
    for dish in dishes:
        num_ingredients = len(cooking_book[dish])
        for i_ingredient in range(num_ingredients):
            name_ingredient = cooking_book[dish][i_ingredient][keys_of_ingredient[0]]
            quantity_ingredient = int(cooking_book[dish][i_ingredient][keys_of_ingredient[1]])
            measure_ingredient = cooking_book[dish][i_ingredient][keys_of_ingredient[2]]
            dict_ingredient = {}
            if name_ingredient in dict_for_shoping:
                dict_for_shoping[name_ingredient][keys_of_ingredient[1]] += quantity_ingredient * person_count
            else:
                dict_ingredient[keys_of_ingredient[2]] = measure_ingredient
                dict_ingredient[keys_of_ingredient[1]] = quantity_ingredient * person_count
                dict_for_shoping[name_ingredient] = dict_ingredient
    return dict_for_shoping

def read_file_create_list(list_names_of_files, root_of_path, mode, coding_type):
    dict_of_files_strings = {}
    list_of_files_num_strings = []
    for name_file in list_names_of_files:
        list_of_file = []
        num_strings_in_file = 0
        full_path_file = os.path.join(root_of_path, name_file)
        with open(full_path_file, mode, encoding=coding_type) as file_of_text:
            eof = False
            while not eof:
                string_of_file = file_of_text.readline().rstrip()
                if not string_of_file:
                    eof = True
                else:
                    list_of_file.append(string_of_file)
                    num_strings_in_file += 1
            dict_of_files_strings[name_file] = list_of_file
            list_of_files_num_strings.append([num_strings_in_file, name_file])
            list_of_files_num_strings.sort()
    return [list_of_files_num_strings, dict_of_files_strings]

def write_result_file(root_of_path, file_name, mode, coding_type, list_of_read_file_create_list):
    full_path_result_file = os.path.join(root_of_path,file_name)
    list_of_files_num_strings = list_of_read_file_create_list[0]
    dict_of_files_strings = list_of_read_file_create_list[1]
    print(list_of_files_num_strings)
    print(dict_of_files_strings)
    with open(full_path_result_file, mode, encoding=coding_type) as file_of_result:
        for i_num_strings_name_files in range(len(list_of_files_num_strings)):
            if i_num_strings_name_files == 0:
                print(list_of_files_num_strings[i_num_strings_name_files][1])
                file_of_result.write(list_of_files_num_strings[i_num_strings_name_files][1])
                file_of_result.write('\n' + str(list_of_files_num_strings[i_num_strings_name_files][0]))
            else:
                file_of_result.write('\n'+list_of_files_num_strings[i_num_strings_name_files][1])
                file_of_result.write('\n'+str(list_of_files_num_strings[i_num_strings_name_files][0]))
            for string_of_file in dict_of_files_strings[list_of_files_num_strings[i_num_strings_name_files][1]]:
                file_of_result.write('\n'+string_of_file)
    return


FILE_NAMES = ['recipes.txt', 'result.txt']
LIST_NAMES_FILES = ['1.txt', '2.txt', '3.txt']
KEYS_OF_DESCRIPTION_INGREDIENT = ['ingredient_name', 'quantity', 'measure']

ROOT_PATH = os.getcwd()

# Задание 1. Создание книги рецептов
cook_book = create_cook_book(ROOT_PATH, FILE_NAMES[0], "r", "utf-8", KEYS_OF_DESCRIPTION_INGREDIENT)

# Задание 2. Создание списка покупок
list_dishes = list(cook_book.keys())
num_persons = 7
dict_ingredients_for_shoping = get_shop_list_by_dishes(list_dishes, num_persons, KEYS_OF_DESCRIPTION_INGREDIENT, cook_book)

# Задание 3. Чтение данных из заданных файлов, сортировка файлов по возрастанию количества строк в них
#            и запись результатов в результирующий файл
# Чтение данных из заданных файлов и сортировка файлов по возрастанию количества строк в них
list_read_file_create_list = read_file_create_list(LIST_NAMES_FILES, ROOT_PATH, "r", "utf-8")
print(list_read_file_create_list)
# Запись резульатов в результирующий файл
write_result_file(ROOT_PATH, FILE_NAMES[1], "w", "utf-8", list_read_file_create_list)