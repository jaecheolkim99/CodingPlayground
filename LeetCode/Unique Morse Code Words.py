"""
https://leetcode.com/submissions/detail/422950016/?from=/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3540/

[BEST]
class Solution(object):    
    a = list(string.ascii_lowercase)
    m = [".-","-...","-.-.","-..",".","..-.","--.","....",
               "..",".---","-.-",".-..","--","-.","---",".--.",
               "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    d = dict( zip(a,m) )
    
    def word2morse(self, word):
        morse = ''
        for letter in word:
            morse += self.d[letter]
        return morse
        
    
    def uniqueMorseRepresentations(self, words):
        unique_morses = []
        for word in words:
            morse_word = self.word2morse(word)
            if morse_word not in unique_morses:
                unique_morses.append(morse_word)
        
        print(self.d)
        return len(unique_morses)

"""
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        result = set()
        
        for word in words:
            morse = ""
            for i in range(len(word)):
                morse = morse + (alphabet[ord(word[i]) - ord('a')])
            result.add(morse)
        
        return len(result)   