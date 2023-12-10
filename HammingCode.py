from copy import deepcopy
from random import randint
from math import ceil

import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext

class HammingCode:
    @staticmethod
    def create_sequence_from_double_nested_array(double_nested_array):
        return ''.join([''.join([str(char) for char in nested_array]) for nested_array in deepcopy(double_nested_array)])

    @staticmethod
    def make_mistake_in_vector(vector, num_of_errors):
        vector_copy = deepcopy(vector)
        # # Если хотим чтобы ошибки не накладывались друг на друга - раскоментировать нижнее
        num_memory = []
        # #
        for i in range(randint(0,num_of_errors)):
            # получаем случайный индекс, где необходимо допустить ошибку
            num = randint(0, len(vector_copy) - 1)
            # # Если хотим чтобы ошибки не накладывались друг на друга - раскоментировать нижнее
            # если уже был использован, генерируем другой
            while num in num_memory:
                num = randint(0, len(vector_copy) - 1)
            num_memory.append(num)
            
            # меняем значение бита на противоположное значение
            if (vector_copy[num] == 0):
                vector_copy[num] = 1
            else:
                vector_copy[num] = 0
        return vector_copy

    # делаем произвольное число ошибок (от 0 до num_of_errors) ошибок во всех векторах
    @staticmethod
    def make_mistake_in_vectors(vectors, num_of_errors):
        vectors_copy = deepcopy(vectors)
        for i in range(len(vectors)):
            vectors_copy[i] = HammingCode.make_mistake_in_vector(vectors_copy[i], num_of_errors)
        return vectors_copy


    @staticmethod
    def make_vector_need_len(vector, vector_length):
        vector_copy = deepcopy(vector)
        while len(vector_copy) < vector_length:
            vector_copy.append(0)
        return vector_copy

    @staticmethod
    def correct_mistake_in_code_word(code_word_with_mistake):
        code_word_with_mistake = deepcopy(code_word_with_mistake)
        if (sum(code_word_with_mistake) == 0):
            return code_word_with_mistake
        not_zero_positions = HammingCode.find_not_zero_positions(code_word_with_mistake)
        # print('not_zero_positions', not_zero_positions)
        contr_bits = HammingCode.find_contr_bits(not_zero_positions)
        # print('contr_bits ', contr_bits)
        contr_bits = HammingCode.make_sum_mod_two(contr_bits)
        # print('contr_bits', contr_bits)
        position_of_mistake = int('0b' + ''.join(list(reversed([str(i) for i in contr_bits]))), 2)
        if (position_of_mistake == 0):
            return code_word_with_mistake
        # print('position_of_mistake ', position_of_mistake)
        if (code_word_with_mistake[position_of_mistake-1] == 1):
            code_word_with_mistake[position_of_mistake-1] = 0
        else:
            code_word_with_mistake[position_of_mistake-1] = 1
        
        # print(code_word_with_mistake)
        return code_word_with_mistake

    @staticmethod
    def correct_mistake_in_code_words(code_words_with_mistakes):
        correct_code_words = []
        for code_word_with_mistake in code_words_with_mistakes:
            correct_code_words.append(HammingCode.correct_mistake_in_code_word(code_word_with_mistake))
        return correct_code_words

    @staticmethod
    def set_control_bits(code_word, control_bits):
        control_bits = deepcopy(control_bits)
        code_word = deepcopy(code_word)
        base = 2
        for i in range(0, len(control_bits)):
            code_word[base**i-1] = control_bits[i]
        return code_word

    @staticmethod
    def make_sum_mod_two(vectors):
        vectors = deepcopy(vectors)
        result = []

        for numbers in zip(*vectors):
            sum_of_numbers = sum(numbers)
            result.append(sum_of_numbers)
        # print(result)
        for i in range(len(result)):
            if (result[i] % 2 == 0):
                result[i] = 0
            else:
                result[i] = 1

        return result

    @staticmethod
    def add_empty_contr_bits(code_word, m):
        code_word = deepcopy(code_word)
        base = 2
        for i in range(0, m):
            code_word.insert(base**i-1, 0)
        return code_word

    @staticmethod
    def find_not_zero_positions(code_word_with_empty_contr_bits):
        code_word_with_empty_contr_bits = deepcopy(code_word_with_empty_contr_bits)
        not_zero_positions = []
        for i in range(len(code_word_with_empty_contr_bits)):
            if code_word_with_empty_contr_bits[i] == 1:
                not_zero_positions.append(i+1)
        return not_zero_positions

    @staticmethod
    def find_contr_bits(not_zero_positions):
        not_zero_positions = deepcopy(not_zero_positions)
        not_zero_positions = [list(bin(i)[2:]) for i in not_zero_positions]
        for i in range(len(not_zero_positions)):
            for j in range(len(not_zero_positions[i])):
                not_zero_positions[i][j] = int(not_zero_positions[i][j])
        need_len = 4 # не может быть больше 11
        not_zero_positions = [HammingCode.make_vector_need_len(list(reversed(not_zero_position)), need_len) for not_zero_position in not_zero_positions]
        return not_zero_positions

    @staticmethod
    def get_binom_vector(vector):
        vector_copy = deepcopy(vector)
        for i in range(len(vector_copy)):
            if vector_copy[i] % 2 == 0:
                vector_copy[i] = 0
            else:
                vector_copy[i] = 1
        return vector_copy

    # получаем информационное слово из кодового путём целочисленного деления кодового слова на порождающий полином
    @staticmethod
    def get_inf_word_from_code_word(code_word, m):

        code_word = deepcopy(code_word)
        base = 2
        for i in range(m-1, -1, -1):
            # print(base**i-1)
            del code_word[base**i-1]
        return code_word

    # получаем информационные слова из кодовых слов
    @staticmethod
    def get_inf_words_from_code_words(code_words, m):
        decoded_inf_words = []
        for code_word in code_words:
            decoded_inf_words.append(HammingCode.get_inf_word_from_code_word(code_word, m))
        return decoded_inf_words

    @staticmethod
    def get_inf_words(text, len_of_inf_word, need_len_to_make_char_from_inf_word):
        inf_words = [bin(ord(char))[2:] for char in list(text)] # преобразуем текст в массив по типу: ['110001', '110010', '110011', '1010']
        for i in range(len(inf_words)):
            inf_words[i] = list(inf_words[i]) # преобразуем каждый элемент массива в список: '110001' -> ['1', '1', '0', '0', '0', '1']
            inf_words[i] = [int(num) for num in inf_words[i]] # преобразуем каждый элемент массива в список чисел: [1, 1, 0, 0, 0, 1]
            inf_words[i].reverse() # разворачиваем каждый элемент массива: [1, 1, 0, 0, 0, 1] -> [1, 0, 0, 0, 1, 1]

            # делаем каждый элемент массива необходимой длины: [1, 0, 0, 0, 1, 1] -> [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
            inf_words[i] = HammingCode.make_vector_need_len(inf_words[i], need_len_to_make_char_from_inf_word)

            # преобразуем каждый элемент массива в строку: [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] -> 110001000000
            inf_words[i] = ''.join([str(num) for num in inf_words[i]])
        
        # преобразовать весь массив инф слов в одну последовательность цифр
        inf_words = [int(char) for char in list(''.join(inf_words))]

        # считаем количество информационных слов необходимой длины, а именно 7
        count_of_inf_word_need_len = ceil(len(inf_words) // len_of_inf_word) + 1

        # добавляем в конец последовательности необходимое число нули, чтобы потом разделить эту последователность на
        # информационные слова одинаковой длины
        inf_words = HammingCode.make_vector_need_len(inf_words, len_of_inf_word * count_of_inf_word_need_len)
        inf_words_need_len = []

        # делим эту последователность на информационные слова одинаковой длины
        for j in range(count_of_inf_word_need_len): inf_words_need_len.append(inf_words[j*len_of_inf_word:(j+1)*len_of_inf_word])
        
        return inf_words_need_len

    @staticmethod
    def make_char_from_inf_words(inf_words, need_len_to_make_char_from_inf_word):
        decoded_text = ''
        text = deepcopy(inf_words)
        # преобразовываем информационные слова в последовательность информационных слов
        for i in range(len(text)):
            text[i] = ''.join([str(char) for char in text[i]])
        text = ''.join(text)

        # получаем символ из каждого куска последовательности информационных слов
        # и добавляем данный символ к переменной decoded_text
        for j in range(len(text)//need_len_to_make_char_from_inf_word):
            # decoded_text += chr(int('0b' + ''.join(reversed(list(text[j*need_len_to_make_char_from_inf_word:(j+1)*need_len_to_make_char_from_inf_word]))), 2))
            decoded_text += chr(int('0b' + ''.join(reversed(list(text[j*need_len_to_make_char_from_inf_word:(j+1)*need_len_to_make_char_from_inf_word]))), 2))
        return decoded_text

    @staticmethod
    def get_code_words_from_inf_words(inf_words, m):
        code_words = deepcopy(inf_words)
        final_code_words = []
        for i in range(len(code_words)):
            code_word_with_empty_contr_bits  = HammingCode.add_empty_contr_bits(code_words[i], m)
            # print(code_word_with_empty_contr_bits)
            not_zero_positions = HammingCode.find_not_zero_positions(code_word_with_empty_contr_bits)
            # print(not_zero_positions)
            contr_bits = HammingCode.find_contr_bits(not_zero_positions)
            # print(contr_bits)
            contr_bits = HammingCode.make_sum_mod_two(contr_bits)
            # print(contr_bits)
            code_word_with_control_bits = HammingCode.set_control_bits(code_word_with_empty_contr_bits, contr_bits)
            # print(code_word_with_control_bits)
            final_code_words.append(code_word_with_control_bits)
        return final_code_words


    @staticmethod
    def code(text, num_of_errors):
        m = 4 # 11 - 7 = 4 количество контрольных битов
        num_of_errors = num_of_errors # количество ошибок, исправляемых
        len_of_inf_word = 8
        need_len_to_make_char_from_inf_word = 12
        text = text
        inf_words = HammingCode.get_inf_words(text, len_of_inf_word, need_len_to_make_char_from_inf_word)

        code_words = HammingCode.get_code_words_from_inf_words(inf_words, m)
        code_words_with_mistake = HammingCode.make_mistake_in_vectors(code_words, num_of_errors)

        return {
            'initial_text': text,
            'inf_words': inf_words,
            'code_words': code_words,
            'code_words_with_mistake': code_words_with_mistake,
        }

        # return {
        #     'initial_text': text,
        #     'inf_words': HammingCode.create_sequence_from_double_nested_array(inf_words),
        #     'code_words': HammingCode.create_sequence_from_double_nested_array(code_words),
        #     'code_words_with_mistake': HammingCode.create_sequence_from_double_nested_array(code_words_with_mistake),
        # }

    @staticmethod
    def decode(code_words):
        code_words_text = code_words.strip()
        code_words = []
        code_word_len = 12
        print(123)
        # print(list(code_words_text))
        try:
            code_words = [int(i) for i in list(code_words_text)]
            # print('code_words', code_words)
        except:
            return False 
        if any(i not in [0, 1] for i in code_words):
            return False
        code_words = [code_words[i:i+code_word_len] for i in range(0, len(code_words), code_word_len)]
        if (len(code_words[-1]) < code_word_len):
            code_words[-1] = HammingCode.make_vector_need_len(code_words[-1], code_word_len)
        # print(code_words)
        m = 4 # 11 - 7 = 4 количество контрольных битов
        need_len_to_make_char_from_inf_word = 12
        code_words_with_mistake = code_words
        # print('code_words_with_mistake ', code_words_with_mistake)
        code_words_without_mistake = HammingCode.correct_mistake_in_code_words(code_words_with_mistake)
        # print('code_words_without_mistake ', code_words_without_mistake)
        decoded_inf_words = HammingCode.get_inf_words_from_code_words(code_words_without_mistake, m)
        # print('decoded_inf_words ', decoded_inf_words)
        decoded_text = HammingCode.make_char_from_inf_words(decoded_inf_words, need_len_to_make_char_from_inf_word)
        # print('decoded_text ', decoded_text == text)
        # print(HammingCode.create_sequence_from_double_nested_array(code_words_with_mistake) == HammingCode.create_sequence_from_double_nested_array(code_words_without_mistake))

        return {
            'decoded_text': decoded_text,
            'decoded_inf_words': HammingCode.create_sequence_from_double_nested_array(decoded_inf_words),
            'code_words_with_mistake': HammingCode.create_sequence_from_double_nested_array(code_words_with_mistake),
            'code_words_without_mistake': HammingCode.create_sequence_from_double_nested_array(code_words_without_mistake)
        }

# print(HammingCode.code('aoksjndfhbnasdf', 1)['code_words_with_mistake'])

# class SecondWindow(tk.Toplevel):
#     def __init__(self, master=None, result=None):
#         super().__init__(master)
#         self.title('Циклические коды, окно вывода данных')
#         self.minsize(1320, 660)

#         self.f_left = tk.Frame(self)
#         self.f_left.pack(side='left')
#         self.f_left.pack(padx=(10, 10))

#         self.f_right = tk.Frame(self)
#         self.f_right.pack(side='left')
#         self.f_right.pack(padx=(10, 10))

#         self.label1 = tk.Label(self.f_left, text=result['title1'])
#         self.label1.pack(side='top')
#         self.label1.pack(pady=10)

#         self.text_code_words = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
#         self.text_code_words.pack(side='top')
#         self.text_code_words.insert(tk.END, result['code_words'])
        
#         self.label2 = tk.Label(self.f_left, text=result['title2'])
#         self.label2.pack(side='top')
#         self.label2.pack(pady=10)

#         self.text_code_words_with_mistake = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
#         self.text_code_words_with_mistake.pack(side='top')
#         self.text_code_words_with_mistake.insert(tk.END, result['code_words_with_mistake'])
        
#         self.label4 = tk.Label(self.f_right, text=result['title4'])
#         self.label4.pack(side='top')
#         self.label4.pack(pady=10)

#         self.text_inf_words = scrolledtext.ScrolledText(self.f_right, wrap=tk.WORD, height=7)
#         self.text_inf_words.pack(side='top')
#         self.text_inf_words.insert(tk.END, result['inf_words'])
        
#         self.label6 = tk.Label(self.f_right, text=result['title6'])
#         self.label6.pack(side='top')
#         self.label6.pack(pady=10)

#         self.initial_text = scrolledtext.ScrolledText(self.f_right, wrap=tk.WORD, height=7)
#         self.initial_text.pack(side='top')
#         self.initial_text.insert(tk.END, result['initial_text'])
        

# class ThirdWindow(tk.Toplevel):
#     def __init__(self, master=None, result=None):
#         super().__init__(master)
#         self.title('Циклические коды, окно вывода данных')
#         self.minsize(1320, 660)

#         self.f_left = tk.Frame(self)
#         self.f_left.pack(side='left')
#         self.f_left.pack(padx=(10, 10))

#         self.f_right = tk.Frame(self)
#         self.f_right.pack(side='left')
#         self.f_right.pack(padx=(10, 10))
        
#         self.label2 = tk.Label(self.f_left, text=result['title2'])
#         self.label2.pack(side='top')
#         self.label2.pack(pady=10)

#         self.text_code_words_with_mistake = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
#         self.text_code_words_with_mistake.pack(side='top')
#         self.text_code_words_with_mistake.insert(tk.END, result['code_words_with_mistake'])
        
#         self.label5 = tk.Label(self.f_right, text=result['title5'])
#         self.label5.pack(side='top')
#         self.label5.pack(pady=10)

#         self.text_decoded_inf_words = scrolledtext.ScrolledText(self.f_right, wrap=tk.WORD, height=7)
#         self.text_decoded_inf_words.pack(side='top')
#         self.text_decoded_inf_words.insert(tk.END, result['decoded_inf_words'])
    
        
#         self.label7 = tk.Label(self.f_right, text=result['title7'])
#         self.label7.pack(side='top')
#         self.label7.pack(pady=10)

#         self.decoded_text = scrolledtext.ScrolledText(self.f_right, wrap=tk.WORD, height=7)
#         self.decoded_text.pack(side='top')
#         self.decoded_text.insert(tk.END, result['decoded_text'])

# class Main(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry('1200x540')
#         self.minsize(600, 540)
#         self.title('Циклические коды, окно ввода данных')

#         self.f_top_left = tk.Frame(self)
#         self.f_top_left.pack(side='left')
#         self.f_top_left.pack(padx=(20, 0))


#         self.f_top_right = tk.Frame(self)
#         self.f_top_right.pack(side='right')
#         self.f_top_right.pack(padx=(0, 20))


#         self.f_bottom = tk.Frame(self)
#         self.f_bottom.pack(side='bottom')
#         self.f_bottom.pack(padx=(20, 0))

#         self.f_btn = tk.Frame(self)
#         self.f_btn.pack(side='top')

#         self.label_initial_text = tk.Label(self.f_top_left, text='Введите текст, который надо закодировать: ')
#         self.label_initial_text.pack(side='top')
#         self.label_initial_text.pack(pady=(10, 0))

#         self.initial_text = scrolledtext.ScrolledText(self.f_top_left, wrap=tk.WORD, height=20, width=55)
#         self.initial_text.pack(side='top')
#         self.initial_text.pack(pady=(10, 0))

#         self.initial_code_words_text = tk.Label(self.f_top_right, text='Введите кодовые слова, которые надо декодировать: ')
#         self.initial_code_words_text.pack(side='top')
#         self.initial_code_words_text.pack(pady=(10, 0))

#         self.initial_code_words = scrolledtext.ScrolledText(self.f_top_right, wrap=tk.WORD, height=20, width=55)
#         self.initial_code_words.pack(side='top')
#         self.initial_code_words.pack(pady=(10, 0))

#         self.type_hamm_code = tk.Label(self.f_bottom, text='Код хэмминга (11,7)')
#         self.type_hamm_code.pack(side='top')
#         self.type_hamm_code.pack(pady=(10, 0))

#         self.len_params = tk.Label(self.f_bottom, text='Длина кодовых слов: 11. Длина информационных слов: 7.')
#         self.len_params.pack(side='top')
#         self.len_params.pack(pady=(10, 0))

#         self.num_fixed_error = tk.Label(self.f_bottom, text='Количество гарантированно исправляемых ошибок: 1')
#         self.num_fixed_error.pack(side='top')
#         self.num_fixed_error.pack(pady=(10, 0))

#         self.num_of_errors = tk.IntVar()

#         self.label_num_of_errors_text = tk.Label(self.f_bottom, text='Укажите максимальное число ошибок в кодовых словах')
#         self.label_num_of_errors_text.pack(side='top')
#         # self.label_num_of_errors_text.pack(pady=(10, 0))

#         self.checkbutton1 = tk.Checkbutton(self.f_bottom, text="0 Ошибок", variable=self.num_of_errors, onvalue=0)
#         self.checkbutton1.pack(side='left')

#         self.checkbutton2 = tk.Checkbutton(self.f_bottom, text="1 Ошибка", variable=self.num_of_errors, onvalue=1)
#         self.checkbutton2.pack(side='left')


#         button_1 = tk.Button(self.f_top_left, text='Закодировать текст', font='Times 12', command=self.code_text)
#         button_1.pack(side = "bottom")
#         button_1.pack(padx=(0, 20))

#         button_1 = tk.Button(self.f_top_right, text='Декодировать кодовые слова', font='Times 12', command=self.decode_code_words)
#         button_1.pack(side='bottom')
#         button_1.pack(padx=(0, 20))

#     def open_second_window(self, result):
#         self.new_window = SecondWindow(self, result=result)

#     def open_third_window(self, result):
#         self.new_window1= ThirdWindow(self, result=result)
    
#     def code_text(self):
#         try:
#             self.initial_text_var = self.initial_text.get("1.0","end")
#             if (self.initial_text_var.strip() == ''):
#                 messagebox.showwarning(title="Предупреждение", message="Введите текст, который надо закодировать")
#                 return
#         except:
#             messagebox.showwarning(title="Предупреждение", message="Что-то пошло не так")
#             return

#         self.result = HammingCode.code(self.initial_text_var, self.num_of_errors.get())

#         self.open_second_window({
#             'title1': 'Последовательность кодовых слов:',
#             'code_words': self.result['code_words'],
#             'title2': 'Последовательность кодовых слов с ошибками:',
#             'code_words_with_mistake': self.result['code_words_with_mistake'],
#             'title4': 'Последовательность информационных слов:',
#             'inf_words': self.result['inf_words'],
#             'title6': 'Начальный текст:',
#             'initial_text': self.result['initial_text'],
#         })

#     def decode_code_words(self):
#         try:
#             self.initial_code_words_var = self.initial_code_words.get("1.0","end")
#             if (self.initial_code_words_var.strip() == ''):
#                 messagebox.showwarning(title="Предупреждение", message="Введите текст, который надо закодировать")
#                 return
#         except:
#             messagebox.showwarning(title="Предупреждение", message="Что-то пошло не так")
#             return

#         self.result = HammingCode.decode(self.initial_code_words_var)
        
#         if (self.result == False):
#             messagebox.showwarning(title="Предупреждение", message="Указаны неверные значения")
#         else:
#             self.open_third_window({
#                 'title2': 'Последовательность кодовых слов:',
#                 'code_words_with_mistake': self.result['code_words_with_mistake'],
#                 'title5': 'Последовательность информационных слов после декодирования:',
#                 'decoded_inf_words': self.result['decoded_inf_words'],
#                 'title7': 'Текст после кодирования/декодирования:',
#                 'decoded_text': self.result['decoded_text'],
#             })

# if __name__ == "__main__":
#     main = Main()
#     main.mainloop()



            #     'title1': 'Последовательность кодовых слов:',
            # 'code_words': self.result['code_words'],
            # 'title2': 'Последовательность кодовых слов с ошибками:',
            # 'code_words_with_mistake': self.result['code_words_with_mistake'],
            # 'title3': 'Последовательность кодовых слов с исправленными ошибками:',
            # 'code_words_without_mistake': self.result['code_words_without_mistake'],
            # 'title4': 'Последовательность информационных слов:',
            # 'inf_words': self.result['inf_words'],
            # 'title5': 'Последовательность информационных слов после декодирования:',
            # 'decoded_inf_words': self.result['decoded_inf_words'],
            # 'title6': 'Начальный текст:',
            # 'initial_text': self.result['initial_text'],
            # 'title7': 'Текст после кодирования/декодирования:',
            # 'decoded_text': self.result['decoded_text'],