# from HammingCode import HammingCode
# from ConvolutionalCode import ConvolutionalCode
# from InterleaverObj import InterleaverObj


# def run():
#     hamm_code_words = HammingCode.code('ф', 1)['code_words_with_mistake']
#     print('hamm_code_words', hamm_code_words, '\n')
#     interleaver_seq = InterleaverObj.interleaver(hamm_code_words)
#     print('interleaver_seq', interleaver_seq, '\n')
#     conv_code_words_seq = ConvolutionalCode.encode(interleaver_seq)
#     print('conv_code_words_seq', conv_code_words_seq, '\n')
#     conv_inf_words = ConvolutionalCode.decode(conv_code_words_seq)
#     print('conv_inf_words', conv_inf_words, '\n')
#     deinterleaver_seq = InterleaverObj.deinterleaver(conv_inf_words)
#     print('deinterleaver_seq\n', deinterleaver_seq, '\n')
#     hamm_inf_words = HammingCode.decode(deinterleaver_seq)['decoded_text']
#     print('hamm_inf_words\n', hamm_inf_words, '\n')

# run()


from copy import deepcopy

from HammingCode import HammingCode
from ConvolutionalCode import ConvolutionalCode
from InterleaverObj import InterleaverObj


class Cascad:
    @staticmethod
    def create_sequence_from_double_nested_array(double_nested_array):
        return ''.join([''.join([str(char) for char in nested_array]) for nested_array in deepcopy(double_nested_array)])
    
    @staticmethod
    def encode(initial_text, num_of_errors):
        hamm_code_words = HammingCode.code(initial_text, num_of_errors)['code_words_with_mistake']
        print('hamm_code_words', hamm_code_words, '\n')
        interleaver_seq = InterleaverObj.interleaver(hamm_code_words)
        print('interleaver_seq', interleaver_seq, '\n')
        conv_code_words_seq = ConvolutionalCode.encode(interleaver_seq)
        print('conv_code_words_seq', conv_code_words_seq, '\n')
        return {
            'hamm_code_words': Cascad.create_sequence_from_double_nested_array(hamm_code_words),
            'interleaver_seq': interleaver_seq,
            'conv_code_words_seq': conv_code_words_seq,
            
        }
    
    @staticmethod
    def decode(conv_code_words_seq):
        # try:
        conv_inf_words = ConvolutionalCode.decode(conv_code_words_seq)
        print('conv_inf_words', conv_inf_words, '\n')
        deinterleaver_seq = InterleaverObj.deinterleaver(conv_inf_words)
        print('deinterleaver_seq\n', deinterleaver_seq, '\n')
        hamm_decoded_value = HammingCode.decode(deinterleaver_seq)['decoded_text']
        print('hamm_decoded_value\n', hamm_decoded_value, '\n')
        if (hamm_decoded_value == False):
            print(123)
            return
        return {
            'conv_inf_words': Cascad.create_sequence_from_double_nested_array(conv_inf_words),
            'deinterleaver_seq': deinterleaver_seq,
            'hamm_decoded_value': hamm_decoded_value
        }
        # except:
        #     return False

# a = Cascad.encode('asasdasdasdasdasdasdasdd',1)
# b = Cascad.decode(a['conv_code_words_seq'])

# print(Cascad.create_sequence_from_double_nested_array(a['hamm_code_words']) == b['deinterleaver_seq'])

