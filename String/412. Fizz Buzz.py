class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [] #array to store
        #N + 1 to have the last number inclusive
        for i in range(1, n + 1):
            #takes care of divisors
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                #Includes quotes while maintaining the variable
                ans.append(f"{i}")
        return ans