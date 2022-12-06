import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    if path_file in str(instance._data):
        return

    lines = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(data)
    print(data)


def remove(instance: Queue):
    if instance.is_empty():
        return print("Não há elementos")
    data = instance.dequeue()
    print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position: int):
    try:
        data = instance.search(position)
        print(data)
    except IndexError:
        sys.stderr.write('Posição inválida')
