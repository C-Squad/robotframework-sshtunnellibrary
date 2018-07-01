from SSHTunnelLibrary.SSHTunnelKeywords import SSHTunnelKeywords
from SSHTunnelLibrary.version import VERSION

_version_ = VERSION


class SSHTunnelLibrary(SSHTunnelKeywords):
    """
    SSH Tunnel Library creates SSH Tunnel which will help to  interact with systems which can not be accessed directly

    Examples:
        | #  generally 443 for Https, 22 for ssh, 3306 for mysql
        | Start SSH Tunnel | MySshTunnel | <remote_host_ip/name> | 443 | <ssh_server_ip/name> | 22 | <ssh_server_username> |  <ssh_server_password> 
        | ${local_bind_port}= | Get Local Port
        | Stop SSH Tunnel | MySshTunnel

    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'