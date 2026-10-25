class Solution:
    def decodeString(self, s: str) -> str:
        character_stack = []

        for character in s:
            if character != "]":
                character_stack.append(character)
                continue

            inner_characters = []
            while character_stack and character_stack[-1] != "[":
                inner_characters.append(character_stack.pop())

            character_stack.pop()  # Remove opening bracket ("[")

            repeat_digits = []
            while character_stack and character_stack[-1].isdigit():
                repeat_digits.append(character_stack.pop())

            repeat_count = int("".join(reversed(repeat_digits)))
            inner_string = "".join(reversed(inner_characters))
            character_stack.extend(inner_string * repeat_count)

        return "".join(character_stack)
