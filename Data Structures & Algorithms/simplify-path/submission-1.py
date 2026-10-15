class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        components = path.split("/")

        for component in components:
            match component:
                case "" | ".":
                    continue
                case "..":
                    if directories:
                        directories.pop()
                case _:
                    directories.append(component)

        return "/" + "/".join(directories)
