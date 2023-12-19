import os


def get_env_variable(variable_name, default_name=''):
    return os.environ.get(variable_name, default_name)


def parse_comma_str_to_list(comma_sep_str):
    if not comma_sep_str or not isinstance(comma_sep_str, str):
        return []
    return [string.strip() for string in comma_sep_str.split(',') if string]
