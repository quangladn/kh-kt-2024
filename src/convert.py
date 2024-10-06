def read_file(file_source: str):
    file_content = open(file_source, "r", encoding="utf-8").read()
    return file_content


def split_content(content: str):
    return list(content)


def do_all_convert(file_source: str):
    content = read_file(file_source)
    return split_content(content)
