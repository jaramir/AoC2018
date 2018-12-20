from part1 import read, parse


def value(node):
    if node["child"]:
        return sum(
            value(node["child"][idx - 1])
            for idx in node["metadata"]
            if idx > 0 and idx <= len(node["child"])
        )
    return sum(node["metadata"])


if __name__ == '__main__':
    tree = parse(read())

    print value(tree)
