def read():
    return [int(v) for v in open("input").read().split()]


def parse(data):
    child_count = data.pop(0)
    metadata_count = data.pop(0)
    child = [parse(data) for i in range(child_count)]
    metadata = [data.pop(0) for i in range(metadata_count)]
    return {"child": child, "metadata": metadata}


def flatten(node):
    return [node] + [flat
                     for child in node["child"]
                     for flat in flatten(child)]


def value(node):
    return sum(node["metadata"])


if __name__ == '__main__':
    tree = parse(read())

    print sum(value(node) for node in flatten(tree))
