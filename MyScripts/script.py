import os
# manage_path = os.path.abspath(os.path.dirname(__file__)) + os.sep + "manage.py"


def get_process_pid(*filters):
    cmd_str = "ps -ef"
    for filter_item in filters:
        cmd_str += " | grep " + str(filter_item)
    print(cmd_str)
    result = os.popen(cmd_str)
    result_info = result.read()
    result_info = ' '.join(result_info.split())
    if result_info == '':
        return None
    return result_info.split(' ')[1]


def run_script(name):
    cmd_str = 'nohup python %s &' % name
    os.system(cmd_str)

# cmd_pid = get_process_pid("python", "main")
# print(cmd_pid)
# os.system("kill -9 %s" % cmd_pid)
print(__file__)
