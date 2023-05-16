import numpy as np

# Моделирование бинарного симметричного канала.
def binary_symmetric_channel(input_bits, error_probability):
    random_array = np.random.rand(len(input_bits))
    flip_positions = random_array < error_probability
    output_bits = np.logical_xor(input_bits, flip_positions)
    output_bits = output_bits.astype(int)
    return output_bits

# Преобразование слов двоичного кода в символы, bits- двоичное кодовое слово, а G - Порождающая матрица.
def bits_to_char(bits, G):
    k = G.shape[0]
    message_bits = bits[:k]
    index = int(''.join(map(str, message_bits)), 2)
    char = chr(index + ord('a'))
    return char

# Преобразование символов в двоичные кодовые слова, c- символ, а G - Порождающая матрица.
def char_to_bits(c, G): 
    k = G.shape[0]
    index = ord(c) - ord('a')
    message = np.array([int(b) for b in bin(index)[2:]], dtype=int)
    message = np.insert(message, 0, [0 for i in range(k-len(message))])
    codeword = np.dot(message, G) % 2
    return codeword

# для внедрения ошибок в кодовые слова, где probability_snr_db - вероятность ошибки для каждого кодового слова, а file_path - путь к файлу, в который нужно внедрить ошибку (шифрование), G - Порождающая матрица.
def test_decoding_rate(file_path,G,probability_snr_db): #
  text_err=[]
  with open(file_path, 'r') as f:
    text = f.read().lower()
    for c in text:
      codeword = char_to_bits(c, G)
      error_codeword = binary_symmetric_channel(codeword, probability_snr_db)
      text_err.append(bits_to_char(error_codeword))
  return text_err
