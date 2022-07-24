# My try after looking at answer and watching Neetcode: https://www.youtube.com/watch?v=qYlHrAKJfyA

def shortest_equivalent_path(path):

    stack = []
    path = path.split("/")

    for token in path:
        if token not in [".", "/", "", ".."]:
            stack.append(token)
        elif token == "..":
            stack.pop()
        print(stack)

    return "/".join(stack)

path = "sc//./../tc/awk/././"
print(shortest_equivalent_path(path))