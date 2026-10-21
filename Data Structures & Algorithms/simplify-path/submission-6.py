class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        component_characters = []
        component_length = 0

        # Append "/" as a sentinel to process the last component
        for character in path + "/":
            if character != "/":
                if component_length < len(component_characters):
                    component_characters[component_length] = character
                else:
                    component_characters.append(character)

                component_length += 1
                continue

            component = "".join(component_characters[:component_length])
            component_length = 0

            if component == "..":
                if directories:
                    directories.pop()
            elif component not in ("", "."):
                directories.append(component)

        return "/" + "/".join(directories)
