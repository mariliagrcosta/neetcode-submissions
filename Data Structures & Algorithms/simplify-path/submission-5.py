class Solution:
    def simplifyPath(self, path: str) -> str:
        reversed_directories = []
        pending_skips = 0
        components = path.split("/")

        # Each ".." skips the next real name to its left
        for component in reversed(components):
            if component in ("", "."):
                continue

            if component == "..":
                pending_skips += 1
            elif pending_skips:
                pending_skips -= 1
            else:
                reversed_directories.append(component)

        return "/" + "/".join(reversed(reversed_directories))
