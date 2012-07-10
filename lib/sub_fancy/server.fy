require: "msgpack.fy"

class SubFancy Server

require: "server/find_definition"

class SubFancy Server {
  include: FindDefinition

  def self run: host_port {
    host, port = host_port split: ":"
    new: host port: (port to_i) . tap: @{
      run
    }
  }

  def initialize: @host port: @port

  def run {
    server = MessagePack RPC Server new
    server listen: @host port: @port handler: self
    server run
  }
}
