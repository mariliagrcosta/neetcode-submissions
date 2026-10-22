class Solution:
    def decodeString(self, s: str) -> str:
        repeat_counts = []
        previous_strings = []
        current_count = 0
        current_string = ""

        for character in s:
            if character.isdigit():
                current_count = current_count * 10 + int(character)
            elif character == "[":
                repeat_counts.append(current_count)
                previous_strings.append(current_string)
                current_count = 0
                current_string = ""
            elif character == "]":
                repeat_count = repeat_counts.pop()
                previous_string = previous_strings.pop()
                current_string = previous_string + current_string * repeat_count
            else:
                current_string += character

        return current_string
