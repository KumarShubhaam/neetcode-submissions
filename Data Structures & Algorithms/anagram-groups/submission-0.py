class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in lookup.keys():
                lookup[sorted_string].append(string)
            else:
                lookup[sorted_string] = [string]
        # print(lookup)
        result = []
        for arr in lookup.values():
            result.append(arr)
        return result