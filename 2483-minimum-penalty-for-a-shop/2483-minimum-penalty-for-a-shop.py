class Solution:
    def bestClosingTime(self, customers: str) -> int:
        sum_y = sum(map(lambda p: p=='Y', customers))
        print(f'sum_y={sum_y}')
        a = sum_y
        best_closing_pos = 0
        for pos in range(len(customers)):
            pos_c = customers[pos]
            if pos_c == 'Y':
                sum_y -= 1
            else:
                sum_y += 1

            if sum_y < a:
                a = sum_y
                best_closing_pos = pos + 1

        return best_closing_pos