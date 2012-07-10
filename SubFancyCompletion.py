import sublime, sublime_plugin, re
from SubFancy import Client

class SubFancyCompletionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.error_view = self.view.window().get_output_panel("subfancy_errors")
    self.show_error("foo")

  def show_error(self, error):
    edit = self.error_view.begin_edit()
    self.error_view.insert(edit, 0, error)
    self.error_view.end_edit(edit)
    self.view.window().run_command("show_panel", {"panel": "output.subfancy_errors"})


class SubFancyMethodCompletion:
  def on_query_completions(self, view, prefix, locations):
    print prefix
    return [("hello", "world")]


  def on_query_context(self, view, key, operator, operand, match_all):
    pass



completion = SubFancyMethodCompletion()

class SubFancyComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        m = re.search("^source\.fancy.*$", view.scope_name(0))
        if m == None:
            return []

        ret = completion.on_query_completions(view, prefix, locations)
        return ret

    # def on_query_context(self, view, key, operator, operand, match_all):
    #         return completer.on_query_context(view, key, operator, operand, match_all)





