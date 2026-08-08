class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'None'
        encoded = str()
        for word in strs:
            curr = str()
            for char in word:
                curr = "-".join([curr, str(ord(char))])
            curr = curr[1:]
            encoded = "$".join([encoded, curr])

        return encoded

    def decode(self, s: str) -> List[str]:
        words = s.split("$")[1:]
        decoded = []
        for word in words:
            if word == '':
                decoded.append("")
                continue
            chars = word.split("-")
            curr = "".join([chr(int(c)) for c in chars])
            decoded.append(curr)

        return decoded
