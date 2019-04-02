def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagrams = {}
    for s in strs:
        key = tuple(sorted(s))
        anagrams[key] = anagrams.get(key, []) + [s]
    return anagrams.values()