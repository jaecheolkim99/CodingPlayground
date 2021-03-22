"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3681/

[BEST]
class Solution(object):
    def spellchecker(self, wordlist, queries):
        
        # Thsi can be doen in like Trie and other creative ways sticking to this for now
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)

"""
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowel_list = {}
        capital_list = {}
        vowel = ['a','e','i','o','u']
        result = []

        for i, word in enumerate(wordlist):
            word = word.lower()
            if word not in capital_list:
                capital_list[word] = [i]
            else:
                capital_list[word].append(i)

            for v in vowel:
                word = word.replace(v, vowel[0])
            if word not in vowel_list:
                vowel_list[word] = [i]
            else:
                vowel_list[word].append(i)

        for query in queries:
            if query in wordlist:
                result.append(query)
            else:
                query = query.lower()
                if query in capital_list:
                    result.append(wordlist[capital_list[query][0]])
                else:
                    for v in vowel:
                        query = query.replace(v, vowel[0])
                    if query in vowel_list:
                        result.append(wordlist[vowel_list[query][0]])
                    else:
                        result.append("")
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))