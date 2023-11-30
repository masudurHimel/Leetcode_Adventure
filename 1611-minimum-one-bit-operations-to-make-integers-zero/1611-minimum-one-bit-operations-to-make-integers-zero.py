class Solution(object):
    def minimumOneBitOperations(self, n):
        binary_representation = bin(n)[2:]
        length = len(binary_representation)
        is_flipped = False
        result = 0

        for i in range(length, 0, -1):
            current_bit = binary_representation[length - i]

            if not is_flipped and current_bit == '1':
                result += (2**i) - 1
                is_flipped = True
            elif is_flipped and current_bit == '1':
                result -= (2**i) - 1
                is_flipped = False

        return result
