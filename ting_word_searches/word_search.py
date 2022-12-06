from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    list = []
    for i in range(len(instance)):
        search = instance.search(i)
        data = [
            {"linha": index + 1}
            for index, line in enumerate(search["linhas_do_arquivo"])
            if word in line.lower()
        ]
    result = {
            "palavra": word,
            "arquivo": search["nome_do_arquivo"],
            "ocorrencias": data,
        }

    if not len(result["ocorrencias"]) > 0:
        return []

    if result:
        list.append(result)

    return list


def search_by_word(word: str, instance: Queue):
    list = []
    for i in range(len(instance)):
        search = instance.search(i)
        data = [
            {"linha": index + 1, "conteudo": line}
            for index, line in enumerate(search["linhas_do_arquivo"])
            if word in line.lower()
        ]
    result = {
            "palavra": word,
            "arquivo": search["nome_do_arquivo"],
            "ocorrencias": data,
        }

    if not len(result["ocorrencias"]) > 0:
        return []

    if result:
        list.append(result)

    return list
