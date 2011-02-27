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

    it "should not keep before attributes":
        self.f.bar = True
        assert True

    it "verifies that previous bar attr doesnt exist":
        assert self.f.bar == True
#
#
#    it "matches upper case python cases":
#        f = FileCollector(path='/asdf')
#        py_file = "CASE_foo.py"
#        assert f.valid_module_name.match(py_file) 
#
#
#    it "does not match case without underscores":
#        f = FileCollector(path='/asdf')
#        py_file = "casfoo.py"
#        assert f.valid_module_name.match(py_file) == None
#        
#
#    it "does not match if it doesn't start with case_":
#        f = FileCollector(path='/asdf')
#        py_file = "foo_case.py"
#        assert f.valid_module_name.match(py_file) == None
#
#
#    it "matches if it has camelcase":
#        f = FileCollector(path='/asdf')
#        py_file = "CaSe_foo.py"
#        assert f.valid_module_name.match(py_file)
#
#
#    it "does not match if it starts with underscore":
#        f = FileCollector(path='/asdf')
#        py_file = "case_foo.py"
#        assert f.valid_module_name.match(py_file)
