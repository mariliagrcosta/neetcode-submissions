class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        start = 0

        # Append "/" as a sentinel to process the last component
        for end, character in enumerate(path + "/"):
            if character != "/":
                continue

            component = path[start:end]

            if component == "..":
                if directories:
                    directories.pop()
            elif component not in ("", "."):
                directories.append(component)

            start = end + 1

        return "/" + "/".join(directories)
