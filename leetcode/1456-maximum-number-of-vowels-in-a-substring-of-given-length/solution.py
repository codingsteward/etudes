class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowel = vowel_count = 0
        for i in range(len(s)):
            vowel_count += int(s[i] in vowels)
            if i >= k:
                vowel_count -= int(s[i-k] in vowels)
            max_vowel = max(max_vowel, vowel_count)
        return max_vowel 
        
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # build a window of size k first
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        max_count = vowel_count

        for i in range(k, len(s)):
            vowel_count += int(s[i] in vowels)
            vowel_count -= int(s[i-k] in vowels)
            max_count = max(max_count, vowel_count)
        return max_coun
