class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        component_characters = []

        # Append "/" as a sentinel to process the last component
        for character in path + "/":
            if character != "/":
                component_characters.append(character)
                continue

            component = "".join(component_characters)
            component_characters.clear()

            if component == "..":
                if directories:
                    directories.pop()
            elif component not in ("", "."):
                directories.append(component)

        return "/" + "/".join(directories)
