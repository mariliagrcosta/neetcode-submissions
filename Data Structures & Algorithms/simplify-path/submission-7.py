class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        component = ""

        # Append "/" as a sentinel to process the last component
        for character in path + "/":
            if character == "/":
                if component == "..":
                    if directories:
                        directories.pop()
                elif component not in ("", "."):
                    directories.append(component)

                component = ""
            else:
                component += character

        return "/" + "/".join(directories)
