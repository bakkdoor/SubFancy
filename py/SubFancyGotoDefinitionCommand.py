import sublime, sublime_plugin

class SubFancyGotoDefinitionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, "Hello, World!")
