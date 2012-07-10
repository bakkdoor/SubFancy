import sublime, sublime_plugin
from SubFancy import Client

class SubFancyGotoDefinitionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    klass = self.current_class()
    method_name = self.current_method()
    res = Client().call("find_instance_method:in_class:", method_name, klass)
    print res

  def current_class(self):
    return "Array"

  def current_method(self):
    return "inspect"