import os

def get_base_path():
    return os.path.abspath('./')+'\\'

def get_monkey_test_log(file_name):
    return os.path.abspath('./monkey_test/log/' + file_name)

def get_performance_function_test_yaml(file_name):
    return os.path.abspath('./performance_function_test/yaml/' + file_name)

print(get_base_path())