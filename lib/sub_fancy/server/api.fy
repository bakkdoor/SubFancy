class SubFancy Server API {
  class Handler {
    def self included: target_class {
      instance_methods: false . each: |m| {
        alias_name = "__old__#{m}"
        target_class alias_method: alias_name for: m
        method = instance_method: m

        message_with_args = m to_s rest
        if: (method executable total_args > 0) then: {
          message_with_args = m to_s split: ":" . map_with_index: |a i| { "#{a}: \" << arg_#{i} << \""} . join: " "
        }

        target_class class_eval: $ """
          def #{method selector_with_args} {
            \"#{message_with_args} -> \" print
            __old__#{method selector_with_args} . tap: @{ inspect println }
          }
        """
      }
    }
  }
}

require: "api/find_definition"

class SubFancy Server API {
  include: FindDefinition
}