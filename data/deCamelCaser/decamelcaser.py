import re

filename = r"party_role.txt"


class deCamelCaser:
    """
    NOT IMPLEMENTED YET
    TEST VERSION ONLY
    """

    @staticmethod
    def camel_case_split(str):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).upper()


# test
with open(filename) as load_file:
    for line in load_file:
        line.strip()
        with open(f'{filename}_fixed', 'a') as save_file:
            print(deCamelCaser.camel_case_split(line))
            save_file.write(deCamelCaser.camel_case_split(line))
