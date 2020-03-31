from adv_print import contact_dict as c_dict

commands = {'l': 'выводит список контактов телефонной книги',
            'a': 'добавляет контакты в телефонную книгу',
            'd': 'удаляет контакт по основному номеру телефона',
            'c': 'поиск контакта по имени и фамилии',
            'f': 'поиск избранных контактов',
            'h': 'подсказка по командам',
            'q': 'выход их программы'}


class Contact:
    def __init__(self, first_name, second_name, phone, *args, **kwargs):
        self.f_name = first_name
        self.s_name = second_name
        self.phone = phone
        if args:
            self.other_pfones = args
        else:
            self.other_pfones = None
        if kwargs:
            self.add_inf = kwargs
            if kwargs.get('favorite') != None:
                self.add_inf.pop('favorite')
                self.favorite = 'Да'
            else:
                self.favorite = 'Нет'
        else:
            self.add_inf = None

    def __str__(self):
        result_str = f'Имя: {self.f_name}\n' \
                     + f'Фамилия: {self.s_name}\n' \
                     + f'Телефон: {self.phone}\n' \
                     + f'В избранном: {self.favorite}\n'
        if self.other_pfones != None:
            result_str = result_str + 'Дополнительные телефоны:\n'
            for item in self.other_pfones:
                result_str = result_str + f'    {item}\n'
        if self.add_inf != None:
            result_str = result_str + 'Дополнительная информация:\n'
            for key_item, val_item in self.add_inf.items():
                result_str = result_str + f'        {key_item} : {val_item}\n'
        return result_str


class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contacts = list()

    def contact_list(self):
        for item in self.contacts:
            print(item)
            print('*' * 50)

    def add_contact(self, contact_list: list):
        for item in contact_list:
            self.contacts.append(item)
        print(f'Контакты добавлены в телефонную книгу')

    def del_contact(self):
        del_contact = None
        del_number = input('Введите номер основного телефона удаляемого контакта => ')
        for item in self.contacts:
            if item.phone == del_number:
                del_contact = item
        if del_contact:
            self.contacts.remove(del_contact)
            print(f'Контакт с номером основного телефона {del_number} удалён из телефонной книги')
        else:
            print(f'Контакт с номером основного телефона {del_number} в телефонной книге не найден')

    def find_contact(self):
        f_contact = None
        find_name = input('Введите через запятую имя и фамилию контакта для поиска => ').strip().split(',')
        for item in self.contacts:
            if (item.f_name == find_name[0]) and (item.s_name == find_name[1]):
                f_contact = item
        if f_contact:
            print(f_contact)
        else:
            print(f'Контакт с именем {find_name[0]} и фамилией {find_name[1]} в телефонной книге не найден')

    def find_favorites(self):
        for item in self.contacts:
            if item.favorite == 'Да':
                print(item)


def help():
    for k, v in commands.items():
        print(f'<{k}> - {v}')


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', '+81234567809', '+91234567809', '+11234567809', '+21234567809',
                   '+31234567809', '+41234567809', favorite=True, telegram='@jhony', email='jhony@smith.com')
    walt = Contact('Walt', 'White', '+79876543210', '+99876543210', '+29876543210',
                   '+39876543210', '+49876543210', favorite=True, facebook='@walt', email='walt@white.com',
                   instagram='@wwhite')
    teddy = Contact('Teddy', 'Tyler', '+71234567000', '+91234567809', '+11234567809', '+21234567809',
                    '+31234567809', '+41234567809', vk='TeddyTyler', telegram='@teddy', email='teddy@tyler.com')
    david = Contact('David', 'Fincher', '+71234567999', email='david@fincher.com')

    print(f'Контакты: jhon, walt, teddy, david созданы')
    contacts = [jhon, walt, teddy, david]

    phbook_name = 'Main'  # input('Введите название для создаваемой телефонной книги => ').strip()
    my_phbook = PhoneBook(phbook_name)

    while True:
        command = input('Введите команду (для просмотра справки по командам введите <h>) => ')
        if command in commands.keys():
            if command == 'l':
                my_phbook.contact_list()
            elif command == 'a':
                my_phbook.add_contact(contacts)
            elif command == 'd':
                my_phbook.del_contact()
            elif command == 'c':
                my_phbook.find_contact()
            elif command == 'f':
                my_phbook.find_favorites()
            elif command == 'h':
                help()
            elif command == 'q':
                break
        else:
            print('Команда не найдена, повторите ввод... ')
