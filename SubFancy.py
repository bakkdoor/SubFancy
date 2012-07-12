import sys, threading
import msgpackrpc

DefaultHost = "127.0.0.1"
DefaultPort = 52400

class Client:
  def __init__(self, host = DefaultHost, port = DefaultPort):
    self.host = host
    self.port = port
    self._client_ = None
    self.connect()

  def connect(self):
     self._client_ = msgpackrpc.Client(msgpackrpc.Address(self.host, self.port))

  def client(self):
    if self._client_ == None:
      self.connect()
    return self._client_


  def call(self, message, *args):
    return self.client().call(message, *args)