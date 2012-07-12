class SubFancy Server API FindDefinition : SubFancy Server API Handler {
  def nested_class_by_name: class_name {
    outer, *nested = class_name split: " "
    val = Kernel[outer]
    nested each: |n| {
      old = val
      try {
        val = val[n]
      } catch Exception => e {
        *stderr* println: $ e inspect
        val = old
      }
    }

    return val
  }

  def find_file: filename {
    filename = filename to_s substitute: /^lib\// with: ""
    Fancy CodeLoader filename_for: filename
  }

  private: ('nested_class_by_name:, 'find_file:)

  # api methods:

  def find_instance_method: method_name in_class: class_name {
    exec = nested_class_by_name: class_name . instance_method: method_name . executable
    [find_file: (exec file), exec definition_line, exec last_line]
  }

  def find_class_method: method_name in_class: class_name {
    exec = nested_class_by_name: class_name . method: method_name . executable
    [find_file: (exec file), exec definition_line, exec last_line]
  }
}