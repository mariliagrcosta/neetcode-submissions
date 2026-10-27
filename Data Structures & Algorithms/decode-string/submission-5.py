class Solution:
    def decodeString(self, s: str) -> str:
        character_stack = []

        for character in s:
            if character != "]":
                character_stack.append(character)
            else:
                inner_string = ""
                while character_stack[-1] != "[":
                    inner_string = character_stack.pop() + inner_string
                character_stack.pop()  # Remove opening bracket ("[")

                repeat_digits = ""
                while character_stack and character_stack[-1].isdigit():
                    repeat_digits = character_stack.pop() + repeat_digits
                character_stack.append(int(repeat_digits) * inner_string)

        return "".join(character_stack)
