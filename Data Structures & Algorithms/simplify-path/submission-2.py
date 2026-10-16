class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        index = 0
        path_length = len(path)

        while index < path_length:
            # Skip consecutive slashes
            while index < path_length and path[index] == "/":
                index += 1

            # Extract the component name using a second pointer
            start = index
            while index < path_length and path[index] != "/":
                index += 1

            # Resolve the path component
            component = path[start:index]
            if component == "..":
                if directories:
                    directories.pop()
            elif component not in ("", "."):
                directories.append(component)

        return "/" + "/".join(directories)
