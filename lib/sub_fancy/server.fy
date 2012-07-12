require: "msgpack.fy"

class SubFancy Server

require: "server/find_definition"

class SubFancy Server {
  class API {
    include: FindDefinition
  }

  def initialize: @host port: @port

  def run {
    server = MessagePack RPC Server new
    server listen: @host port: @port handler: $ API new
    server run
  }
}
