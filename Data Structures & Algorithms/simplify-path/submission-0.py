class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        components = path.split("/")

        for component in components:
            if component in ("", "."):
                continue

            if component == "..":
                if directories:
                    directories.pop()
            else:
                directories.append(component)

        return "/" + "/".join(directories)
