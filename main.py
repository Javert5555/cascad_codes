from copy import deepcopy
from random import randint
from math import ceil

import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext

from all import Cascad

class SecondWindow(tk.Toplevel):
    def __init__(self, master=None, result=None):
        super().__init__(master)
        self.title('Кодирование')
        self.minsize(750, 660)

        self.f_left = tk.Frame(self)
        self.f_left.pack(side='left')
        self.f_left.pack(padx=(10, 10))

        # self.f_right = tk.Frame(self)
        # self.f_right.pack(side='left')
        # self.f_right.pack(padx=(10, 10))

        self.label1 = tk.Label(self.f_left, text=result['title1'])
        self.label1.pack(side='top')
        self.label1.pack(pady=10)

        self.text_code_words = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
        self.text_code_words.pack(side='top')
        self.text_code_words.insert(tk.END, result['hamm_code_words'])
        
        self.label2 = tk.Label(self.f_left, text=result['title2'])
        self.label2.pack(side='top')
        self.label2.pack(pady=10)

        self.text_code_words_with_mistake = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
        self.text_code_words_with_mistake.pack(side='top')
        self.text_code_words_with_mistake.insert(tk.END, result['interleaver_seq'])
        
        self.label4 = tk.Label(self.f_left, text=result['title4'])
        self.label4.pack(side='top')
        self.label4.pack(pady=10)

        self.text_inf_words = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=7)
        self.text_inf_words.pack(side='top')
        self.text_inf_words.insert(tk.END, result['conv_code_words_seq'])
    
        

class ThirdWindow(tk.Toplevel):
    def __init__(self, master=None, result=None):
        super().__init__(master)
        self.title('Декодирование')
        self.minsize(750, 660)

        self.f_left = tk.Frame(self)
        self.f_left.pack(side='left')
        self.f_left.pack(padx=(10, 10))

        self.f_right = tk.Frame(self)
        self.f_right.pack(side='left')
        self.f_right.pack(padx=(10, 10))
        
        self.label2 = tk.Label(self.f_left, text=result['title2'])
        self.label2.pack(side='top')
        self.label2.pack(pady=10)

        self.text_code_words_with_mistake = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
        self.text_code_words_with_mistake.pack(side='top')
        self.text_code_words_with_mistake.insert(tk.END, result['conv_inf_words'])
        
        self.label5 = tk.Label(self.f_left, text=result['title5'])
        self.label5.pack(side='top')
        self.label5.pack(pady=10)

        self.text_decoded_inf_words = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=7)
        self.text_decoded_inf_words.pack(side='top')
        self.text_decoded_inf_words.insert(tk.END, result['deinterleaver_seq'])
    
        
        self.label7 = tk.Label(self.f_left, text=result['title7'])
        self.label7.pack(side='top')
        self.label7.pack(pady=10)

        self.decoded_text = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=7)
        self.decoded_text.pack(side='top')
        self.decoded_text.insert(tk.END, result['hamm_decoded_value'])

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1400x540')
        self.minsize(600, 540)
        self.title('Циклические коды, окно ввода данных')

        self.f_top_left = tk.Frame(self)
        self.f_top_left.pack(side='left')
        self.f_top_left.pack(padx=(20, 0))


        self.f_top_right = tk.Frame(self)
        self.f_top_right.pack(side='right')
        self.f_top_right.pack(padx=(0, 20))


        self.f_bottom = tk.Frame(self)
        self.f_bottom.pack(side='bottom')
        self.f_bottom.pack(padx=(20, 0))

        self.f_btn = tk.Frame(self)
        self.f_btn.pack(side='top')

        self.label_initial_text = tk.Label(self.f_top_left, text='Введите текст, который надо закодировать: ')
        self.label_initial_text.pack(side='top')
        self.label_initial_text.pack(pady=(10, 0))

        self.initial_text = scrolledtext.ScrolledText(self.f_top_left, wrap=tk.WORD, height=20, width=55)
        self.initial_text.pack(side='top')
        self.initial_text.pack(pady=(10, 0))

        self.initial_code_words_text = tk.Label(self.f_top_right, text='Введите кодовые слова, которые надо декодировать: ')
        self.initial_code_words_text.pack(side='top')
        self.initial_code_words_text.pack(pady=(10, 0))

        self.initial_code_words = scrolledtext.ScrolledText(self.f_top_right, wrap=tk.WORD, height=20, width=55)
        self.initial_code_words.pack(side='top')
        self.initial_code_words.pack(pady=(10, 0))

        self.type_hamm_code = tk.Label(self.f_bottom, text='Код хэмминга (12,8)')
        self.type_hamm_code.pack(side='top')
        self.type_hamm_code.pack(pady=(10, 0))

        self.len_params = tk.Label(self.f_bottom, text='Длина кодовых слов: 12. Длина информационных слов: 8.')
        self.len_params.pack(side='top')
        self.len_params.pack(pady=(10, 0))

        self.num_fixed_error = tk.Label(self.f_bottom, text='Количество гарантированно исправляемых ошибок: 1')
        self.num_fixed_error.pack(side='top')
        self.num_fixed_error.pack(pady=(10, 0))

        self.num_of_errors = tk.IntVar()

        self.label_num_of_errors_text = tk.Label(self.f_bottom, text='Укажите максимальное число ошибок в кодовых словах')
        self.label_num_of_errors_text.pack(side='top')
        # self.label_num_of_errors_text.pack(pady=(10, 0))
        self.checkbutton1 = tk.Checkbutton(self.f_bottom, text="0 Ошибок", variable=self.num_of_errors, onvalue=0)
        self.checkbutton1.pack(side='top')

        self.checkbutton2 = tk.Checkbutton(self.f_bottom, text="1 Ошибка", variable=self.num_of_errors, onvalue=1)
        self.checkbutton2.pack(side='top')

        # 
        self.conv_code = tk.Label(self.f_bottom, text='Свёрточный код')
        self.conv_code.pack(side='top')
        self.conv_code.pack(pady=(30, 0))

        self.conv_params = tk.Label(self.f_bottom, text='3 регистра и 3 сумматора')
        self.conv_params.pack(side='top')
        self.conv_params.pack(pady=(10, 0))

        self.sum1 = tk.Label(self.f_bottom, text='Первый сумматор: [1, 1, 1]')
        self.sum1.pack(side='top')
        self.sum1.pack(pady=(10, 0))

        self.sum2 = tk.Label(self.f_bottom, text='Второй сумматор: [1, 1, 0]')
        self.sum2.pack(side='top')
        self.sum2.pack(pady=(10, 0))

        self.sum3 = tk.Label(self.f_bottom, text='Третий сумматор: [1, 0, 1]')
        self.sum3.pack(side='top')
        self.sum3.pack(pady=(10, 0))
        # 

        button_1 = tk.Button(self.f_top_left, text='Закодировать текст', font='Times 12', command=self.code_text)
        button_1.pack(side = "bottom")
        button_1.pack(padx=(0, 20))

        button_1 = tk.Button(self.f_top_right, text='Декодировать кодовые слова', font='Times 12', command=self.decode_code_words)
        button_1.pack(side='bottom')
        button_1.pack(padx=(0, 20))

    def open_second_window(self, result):
        self.new_window = SecondWindow(self, result=result)

    def open_third_window(self, result):
        self.new_window1= ThirdWindow(self, result=result)
    
    def code_text(self):
        try:
            self.initial_text_var = self.initial_text.get("1.0","end")
            if (self.initial_text_var.strip() == ''):
                messagebox.showwarning(title="Предупреждение", message="Введите текст, который надо закодировать")
                return
        except:
            messagebox.showwarning(title="Предупреждение", message="Что-то пошло не так")
            return

        self.result = Cascad.encode(self.initial_text_var, self.num_of_errors.get())

        self.open_second_window({
            'title1': 'Последовательность кодовых слов кода Хэмминга:',
            'hamm_code_words': self.result['hamm_code_words'],
            'title2': 'Результат работы перемежителя по кодовым словам:',
            'interleaver_seq': self.result['interleaver_seq'],
            'title4': 'Последовательность кодовых слов свёрточного кода:',
            'conv_code_words_seq': self.result['conv_code_words_seq'],
        })

    def decode_code_words(self):
        try:
            self.initial_code_words_var = self.initial_code_words.get("1.0","end")
            if (self.initial_code_words_var.strip() == ''):
                messagebox.showwarning(title="Предупреждение", message="Введите текст, который надо закодировать")
                return
        except:
            messagebox.showwarning(title="Предупреждение", message="Что-то пошло не так")
            return

        self.result = Cascad.decode(self.initial_code_words_var.strip())
        
        if (self.result == False):
            messagebox.showwarning(title="Предупреждение", message="Указаны неверные значения")
        else:
            self.open_third_window({
                'title2': 'Последовательность информационных слов свёрточного кода:',
                'conv_inf_words': self.result['conv_inf_words'],
                'title5': 'Результат работы деперемежителя по информационным словам:',
                'deinterleaver_seq': self.result['deinterleaver_seq'],
                'title7': 'Текст после кодирования/декодирования:',
                'hamm_decoded_value': self.result['hamm_decoded_value'],
            })

if __name__ == "__main__":
    main = Main()
    main.mainloop()



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

#   