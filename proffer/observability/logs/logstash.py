# This is a custom implementation of the logstash handler to fix a bug
# when it runs in the Mac OS platform. The bug is that in Mac OS, the
# TIOCOUTQ system call is not available, so the code will raise an IOError
# when it tries to call it. This implementation checks if the platform is
# Mac OS and if it is, it will return True for the _is_sock_write_buff_empty.
# This will potentially cause the logstash handler to drop some logs, but
# it is not a big issue since Mac OS is mostly used for development purposes.

from sys import platform
from logstash_async.handler import SynchronousLogstashHandler
from logstash_async.constants import constants
from logstash_async.transport import TcpTransport

try:
    import fcntl
    import struct
    import termios
except ImportError:
    fcntl = None

class CustomSynchronousLogstashHandler(SynchronousLogstashHandler):
  def __init__(self, *args, **kwargs):
    transport = 'customTcpTransport'
    super().__init__(*args, transport=transport, **kwargs)


  def _setup_transport(self, **kwargs):
    if self._transport_path == 'customTcpTransport':
      transport_args = dict(
            host=self._host,
            port=self._port,
            timeout=constants.SOCKET_TIMEOUT,
            ssl_enable=self._ssl_enable,
            ssl_verify=self._ssl_verify,
            keyfile=self._keyfile,
            certfile=self._certfile,
            ca_certs=self._ca_certs,
            **kwargs)
      
      self._transport = CustomTcpTransport(**transport_args)
    else:
      super()._setup_transport(**kwargs)


class CustomTcpTransport(TcpTransport):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def _is_sock_write_buff_empty(self):
    if fcntl is None or platform == 'darwin':
        return True
    socket_fd = self._sock.fileno()
    buffer_size = struct.pack('I', 0)
    ioctl_result = fcntl.ioctl(socket_fd, termios.TIOCOUTQ, buffer_size)
    buffer_size = struct.unpack('I', ioctl_result)[0]
    return not buffer_size