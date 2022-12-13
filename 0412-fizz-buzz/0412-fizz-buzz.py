class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                print(i)
                r = "FizzBuzz"
            elif i%3 == 0:
                r = "Fizz"
            elif i%5 == 0:
                r = "Buzz"
            else:
                r = f"{i}"
            res.append(r)
        return res