"""
You are playing the following Bulls and Cows game with your friend: 
 You write down a number and ask your friend to guess what the number is. 
 Each time your friend makes a guess, you provide a hint that indicates
 how many digits in said guess match your secret number exactly in both digit
 and position (called "bulls") and how many digits match the secret number 
 but locate in the wrong position (called "cows"). 
 Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, 
use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

[BEST]
class Solution(object):
    def getHint(self, secret, guess):        
        bulls = sum(secret[i] == guess[i] for i in range(len(guess)))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return "{}A{}B".format(bulls, both-bulls)
"""

class Solution(object):
    def getHint(self, secret, guess):
        match_a = 0
        match_b = 0

        secret_remain = []
        guess_remain = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                match_a += 1
            else:
                secret_remain.append(int(secret[i]))
                guess_remain.append(int(guess[i]))

        secret_remain = sorted(secret_remain)
        guess_remain = sorted(guess_remain)

        end_remain = len(secret_remain)
        i = j = 0

        while (i != end_remain and j != end_remain):
            if secret_remain[i] == guess_remain[j]:
                match_b += 1
                i += 1
                j += 1
            elif secret_remain[i] > guess_remain[j]:
                j += 1
            else:
                i += 1

        return "{}A{}B".format(match_a, match_b)

if __name__ == '__main__':
    s = Solution()

    print(s.getHint("1123", "5111"))