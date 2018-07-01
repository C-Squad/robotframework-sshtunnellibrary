import sshtunnel

from robot.utils import ConnectionCache

class SSHTunnelKeywords(object):
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._connections = ConnectionCache()
    
    @property
    def current(self):
        return self._connections.current

    def start_ssh_tunnel(
            self, 
            alias, 
            remote_host_ip, 
            remote_host_port, 
            ssh_server_ip, 
            ssh_server_port, 
            ssh_server_username, 
            ssh_server_password,
            local_host_ip='127.0.0.1',
            local_host_port=0):
        
        """ Starts SSH Tunnel to give remote host via SSH Server
        ``alias`` Robot framework alias to find the session
        ``remote_host_ip`` IP of remote host
        ``remote_host_port`` Port number of remote host to connect
        ``ssh_server_ip`` SSH Server which has connection to remote host. 
        ``ssh_server_port`` SSH Port of SSH Server. Usually it is 22
        ``ssh_server_username`` User name of SSH Server
        ``ssh_server_password`` Password of SSH Server
        ``local_host_ip`` Local host IP.  It can be IP or '127.0.0.1'. It is optional variable, default value is  "127.0.0.1"
        ``local_host_port`` Local port to map, default is 0 and 0 means any available port

        returns the connection index
        """

        sshtunnel.DAEMON = True
        server = sshtunnel.SSHTunnelForwarder(
            (ssh_server_ip, ssh_server_port),
            ssh_username=ssh_server_username,
            ssh_password=ssh_server_password,
            remote_bind_address=(remote_host_ip, remote_host_port),
            local_bind_address=(local_host_ip, local_host_port)
        )
        server.start()
        connection_index = self._connections.register(server, alias)
        return connection_index
    
    def stop_ssh_tunnel(self, index_or_alias=''):
        """ Stops the specifc SSH Tunnel using its index or alias
        ``index_or_alias`` Index or Alias of the session to be closed
        
        returns none
        """
        
        if index_or_alias != '':
            try:
                self.switch_connection(index_or_alias)
                self.current.stop()              
                self._connections.current = self._connections._no_current
            except:
                pass

    def switch_connection(self, index_or_alias):
        """ Switch to the specific session using its index or alias.
        ``index_or_alias`` Index or Alias of the session to switch

        returns previous sesssion index
        """
        
        old_index = self._connections.current_index
        if index_or_alias is None:
            self.stop_ssh_tunnel()
        else:
            self._connections.switch(index_or_alias)
        return old_index

    def get_local_port(self):
        """ Gets the current local port whicch is bind to remote port

        returns the local port where it binds
        """

        return self.current.local_bind_port

    def connection_exists(self, index_or_alias):
        """ Validates whether connection or session exists or not
        ``index_or_alias Index or Alias of the session to be validate of its existance

        returns True if connection exists, False otherwise
        """

        try:
            index = self._connections._resolve_alias_or_index(index_or_alias)
            return True
        except ValueError:
            return False
    
    def stop_all_ssh_tunnel(self):
        """  Stops all the SSH Tunnel sessions
        """

        try:
            self._connections.close_all(closer_method='stop')
        except:
            pass