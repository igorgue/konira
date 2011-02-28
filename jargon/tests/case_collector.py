# coding: jargon

from jargon.collector import FileCollector


describe "collect paths":


    before_each:
        self.f = FileCollector(path='/asdf')


    it "should be a list":
        assert isinstance(self.f, list)


    it "does not match normal python files":
        py_file = "foo.py"
        assert self.f.valid_module_name.match(py_file) == None


    it "matches upper case python cases":
        py_file = "CASE_foo.py"
        assert self.f.valid_module_name.match(py_file) 


    it "does not match case without underscores":
        py_file = "casfoo.py"
        assert self.f.valid_module_name.match(py_file) == None
        

    it "does not match if it doesn't start with case_":
        py_file = "foo_case.py"
        assert self.f.valid_module_name.match(py_file) == None


    it "matches if it has camelcase":
        py_file = "CaSe_foo.py"
        assert self.f.valid_module_name.match(py_file)


    it "does not match if it starts with underscore":
        py_file = "case_foo.py"
        assert self.f.valid_module_name.match(py_file)