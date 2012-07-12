require: "msgpack.fy"

class SubFancy Server

require: "server/api"

class SubFancy Server {
  def initialize: @host port: @port

  def run {
    server = MessagePack RPC Server new
    server listen: @host port: @port handler: $ API new
    server run
  }
}
