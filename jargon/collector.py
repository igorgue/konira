import os
import re



class FileCollector(list):


    def __init__(self, path, match):
        self.match             = match
        self.path              = path
        self.valid_module_name = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)
        self._collect()


    def _collect(self):
        for root, dirs, files in os.walk(self.path):
            for item in files:
                absolute_path = os.path.join(root, item)
                if not self.valid_module_name.match(item):
                    continue
                if item.lower().endswith("py"):
                    if "case" in item.lower():
                        self.append(absolute_path)



def globals_from_execed_file(filename):
    globals_ = {}
    execfile(filename, globals_)
    return globals_

