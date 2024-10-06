class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        goodStrs = []

        if len(words) > 1000 or len(chars) > 100:
            return 0

        for w in words:
            if len(w) > 100:
                return

            isGoodStr = True
            usedIdxs = []

            for c in w:
                charsCopy = [
                    d if j not in usedIdxs else "_" for j, d in enumerate(chars)
                ]

                if c not in charsCopy:
                    isGoodStr = False
                    break
                charIdx = charsCopy.index(c)
                usedIdxs.append(charIdx)

            if isGoodStr:
                goodStrs.append(w)

        return sum([len(w) for w in goodStrs])
