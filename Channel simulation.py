import numpy as np

def binary_symmetric_channel(input_bits, error_probability):
    random_array = np.random.rand(len(input_bits))
    flip_positions = random_array < error_probability
    output_bits = np.logical_xor(input_bits, flip_positions)
    output_bits = output_bits.astype(int)
    return output_bits