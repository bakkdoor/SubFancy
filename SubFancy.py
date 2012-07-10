import sys
import msgpackrpc

DefaultHost = "127.0.0.1"
DefaultPort = 52400

class Client:
  def __init__(self, host = DefaultHost, port = DefaultPort):
    self.host = host
    self.port = port
    self.client = None
    self.connect()

  def connect(self):
    if self.client == None:
      self.client = msgpackrpc.Client(msgpackrpc.Address(self.host, self.port))
    return self.client


  def call(self, message, *args):
    if self.client == None:
      self.connect()
    return self.client.call(message, *args)