import sublime, sublime_plugin
from SubFancy import Client

class SubFancyGotoDefinitionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.error_view = self.view.window().get_output_panel("subfancy_errors")
    klass = self.current_class()
    method_name = self.current_method()
    res = None
    try:
      res = Client().call("find_instance_method:in_class:", method_name, klass)
    except Exception, e:
      self.show_error(e.message)
      return

    if res == None:
      self.show_error("Something went wrong :(")
      return

    self.file = res[0]
    self.line = res[1]
    self.new_view = self.view.window().open_file(self.file)
    sublime.set_timeout(self.goto_line, 100)

  def goto_line(self):
    self.new_view.run_command("goto_line", {"line": self.line})

  def show_error(self, error):
    edit = self.error_view.begin_edit()
    self.error_view.insert(edit, 0, error)
    self.error_view.end_edit(edit)
    self.view.window().run_command("show_panel", {"panel": "output.subfancy_errors"})

  def current_class(self):
    return "FutureSend"

  def current_method(self):
    return "value"