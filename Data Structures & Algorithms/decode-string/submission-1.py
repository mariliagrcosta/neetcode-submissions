class Solution:
    def decodeString(self, s: str) -> str:
        frame_stack = []
        current_count = 0
        current_string = ""

        for character in s:
            if character.isdigit():
                current_count = current_count * 10 + int(character)
            elif character == "[":
                frame_stack.append((current_string, current_count))
                current_count = 0
                current_string = ""
            elif character == "]":
                previous_string, repeat_count = frame_stack.pop()
                current_string = previous_string + current_string * repeat_count
            else:
                current_string += character

        return current_string
