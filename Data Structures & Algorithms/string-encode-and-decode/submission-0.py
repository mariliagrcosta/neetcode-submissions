class Solution:

    def encode(self, strs: List[str]) -> str:  
        encoded_string = []

        for s in strs:
            encoded_string.append(f"{len(s)}:{s}")

        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        index = 0

        while index < len(s):
            separator_idx = s.find(":", index)
            length = int(s[index:separator_idx])
            index = separator_idx + 1
            decoded_strings.append(s[index:index + length])
            index += length

        return decoded_strings
