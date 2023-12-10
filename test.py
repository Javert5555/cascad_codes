# from copy import deepcopy

# from HammingCode import HammingCode
# from ConvolutionalCode import ConvolutionalCode
# from InterleaverObj import InterleaverObj


# class Cascad:
#     @staticmethod
#     def create_sequence_from_double_nested_array(double_nested_array):
#         return ''.join([''.join([str(char) for char in nested_array]) for nested_array in deepcopy(double_nested_array)])
    
#     @staticmethod
#     def encode(initial_text, num_of_errors):
#         hamm_code_words = HammingCode.code(initial_text, num_of_errors)['code_words_with_mistake']
#         print('hamm_code_words', hamm_code_words, '\n')
#         interleaver_seq = InterleaverObj.interleaver(hamm_code_words)
#         print('interleaver_seq', interleaver_seq, '\n')
#         conv_code_words_seq = ConvolutionalCode.encode(interleaver_seq)
#         print('conv_code_words_seq', conv_code_words_seq, '\n')
#         return {
#             'hamm_code_words': Cascad.create_sequence_from_double_nested_array(hamm_code_words),
#             'interleaver_seq': interleaver_seq,
#             'conv_code_words_seq': conv_code_words_seq,
            
#         }
    
#     @staticmethod
#     def decode(conv_code_words_seq):
#         try:
#             conv_inf_words = ConvolutionalCode.decode(conv_code_words_seq)
#             print('conv_inf_words', conv_inf_words, '\n')
#             deinterleaver_seq = InterleaverObj.deinterleaver(conv_inf_words)
#             print('deinterleaver_seq\n', deinterleaver_seq, '\n')
#             hamm_decoded_value = HammingCode.decode(deinterleaver_seq)['decoded_text']
#             print('hamm_decoded_value\n', hamm_decoded_value, '\n')
#             if (hamm_decoded_value == False):
#                 print(123)
#                 return
#             return {
#                 'conv_inf_words': Cascad.create_sequence_from_double_nested_array(conv_inf_words),
#                 'deinterleaver_seq': deinterleaver_seq,
#                 'hamm_decoded_value': hamm_decoded_value
#             }
#         except:
#             return False

# # Cascad.encode('asd',2)
# # Cascad.decode('000111111100011100111100100011100111000000000000000111000011000000000111000000000000000000000111111011011000000111111011011000111000011000000000000000000000000000111000011111000100')





























# import numpy as np
# from numpy.polynomial import Polynomial

# '111000011000000111111011011000000000111111100100011100111011011000000000000111000100000100111011011000000000000000111000011111111011011000000000111111011011111111100011011000000000000111111011011111111011011000000000000111111100011100111011011000000000111000011111000100111011011000000000000111000100000100111011011000000000000011011000000000000000111000011111111011011000000000111000011111000100111011011000000000000111111011011111111011011000000000000111111100011100111011011000000000'
# print(bin(ord('a'))[2:])

# print('001001010000010010000011000100000100000001100110101101001000' == '001001010000010010000011000100000100000001100110101101001000')

# arr = np.array(list('123456789')).reshape(1, 9)

# print(arr)


# print('011000000110000100001111110011000000001010100110000000000000' == '011000000110000100001111110011000000001010100110000000000000')
# print('aaknsdfjnvokMNZJDkfnook' == 'aaknsdfjnvokMNZJDkfnook')

# # arr = [[0, 0, 1], [1, 0, 1], [1, 0, 1]]
# # for i in arr:
# #     print(Polynomial(i))

# print(len(list('001000011000100011000111100011110000101000000100000100001011000100110000100000000100')))
# print(len(list('100101010010100001001101100101000010000110001100000001000101000000000010000000001000')))


from CascadCode import Cascad
Cascad.encode('asd',1)
Cascad.decode('000111111100011100111100100011100111000000000000000111000011000000000111000000000000000000000111111011011000000111111011011000111000011000000000000000000000000000111000011111000100')
