class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for i in strs:
            sorted_word = ''.join(sorted(i))
            anagram_map[sorted_word].append(i)

        return list(anagram_map.values())