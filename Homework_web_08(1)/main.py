from conf.models import Author, Quote

from conf.heandlers import find_by_author, find_by_tag, find_by_tags

def search():
    while True:
        command = input("Enter in format 'key:value/values(sep by coma'): >>")
        if command == "exit":
            break
        sep_com = command.split(':')
        if sep_com[0].strip() == "name":
            print(find_by_author(sep_com[1].strip()))
        if sep_com[0].strip() == "tag":
            print(find_by_tag(sep_com[1].strip()))
        if sep_com[0].strip() == "tags":
            sepcom_list = sep_com[1].split(',')
            sepcom_strip = [el.strip() for el in sepcom_list]
            print(sepcom_strip)
            print(find_by_tags(sepcom_strip))


if __name__ == '__main__':
    search()