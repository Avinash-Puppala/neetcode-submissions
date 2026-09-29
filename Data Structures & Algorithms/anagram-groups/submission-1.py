class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultmap = defaultdict(list)
        for i in strs:
            sorted_key = "".join(sorted(i))
            resultmap[sorted_key].append(i)
        return list(resultmap.values())
            