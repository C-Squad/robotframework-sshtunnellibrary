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

        sshtunnel.DAEMON = True
        server = sshtunnel.SSHTunnelForwarder(
            (ssh_server_ip, ssh_server_port),
            ssh_username=ssh_server_username,
            ssh_password=ssh_server_password,
            remote_bind_address=(remote_host_ip, remote_host_port),
            local_bind_address=(local_host_ip, local_host_port)
        )
        server.start()
        connection_index = self._connections.register(server, str_alias)
        return connection_index
    
    def stop_ssh_tunnel(self, index_or_alias=''):

        if index_or_alias != '':
            try:
                self.switch_connection(index_or_alias)
                self.current.stop()              
                self._connections.current = self._connections._no_current
            except:
                pass

    def switch_connection(self, index_or_alias):

        old_index = self._connections.current_index
        if index_or_alias is None:
            self.stop_ssh_tunnel()
        else:
            self._connections.switch(index_or_alias)
        return old_index

    def get_local_port(self):
        
        return self.current.local_bind_port

    def connection_exist(self, index_or_alias):
        
        try:
            index = self._connections._resolve_alias_or_index(index_or_alias)
            return True
        except ValueError:
            return False
    
    def stop_all_ssh_tunnel(self):
        
        try:
            self._connections.close_all(closer_method='stop')
        except:
            pass