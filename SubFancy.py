import sys, threading
import msgpackrpc

DefaultHost = "127.0.0.1"
DefaultPort = 52400

LOCAL = threading.local()
LOCAL.msgpack_client = None

class Client:
  def __init__(self, host = DefaultHost, port = DefaultPort):
    self.host = host
    self.port = port
    self.client = LOCAL.msgpack_client
    if self.client == None:
      self.connect()

  def connect(self):
    LOCAL.msgpack_client = msgpackrpc.Client(msgpackrpc.Address(self.host, self.port))
    self.client = LOCAL.msgpack_client


  def call(self, message, *args):
    if self.client == None:
      self.connect()
    return self.client.call(message, *args)