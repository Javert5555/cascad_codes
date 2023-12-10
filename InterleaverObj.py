import numpy as np
# from HammingCode import HammingCode

class InterleaverObj:
    @staticmethod
    def interleaver(arr):
        len_codeword = 12
        # arr = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]]
        # for i in arr:
            # print(i)
        arr_copy = np.concatenate(arr)
        matrix = arr_copy.reshape(int(len(arr_copy)/len_codeword), len_codeword)
        print(matrix)
        # result = matrix.ravel()
        result = ''.join(matrix.flatten('F').astype(str))
        return ''.join([str(i) for i in result])
    
    @staticmethod
    def deinterleaver(arr):
        # arr = np.concatenate(np.array(arr))
        # print(arr)
        len_codeword = 12
        arr_copy = np.concatenate(arr)
        # print(len(arr_copy)/len_codeword)
        matrix = arr_copy.reshape(len_codeword, int(len(arr_copy)/len_codeword))
        matrix = np.transpose(matrix)
        # Преобразовать массив в матрицу с 11 столбцами
        # matrix = new_arr.reshape(-1, 12)
        print(matrix)

        # Считать по строкам в одну строку
        result = matrix.ravel()
        return ''.join([str(i) for i in result])

# print('result', InterleaverObj.interleaver(HammingCode.code('aok', 1)['code_words_with_mistake']))
# print('result', InterleaverObj.deinterleaver([[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 
# 0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]))