import unittest
from SSHTunnelLibrary import SSHTunnelLibrary
SSHTunnelLibrary
class Test_ssh_keywords(unittest.TestCase): 
    def setUp(self):
        print ("\n####### Test Started #######\n")
        self.obj_ssh_tunnel_lib = SSHTunnelLibrary()
        print ("\nsetup done\n") 

    def tearDown(self):               
        self.obj_ssh_tunnel_lib.stop_all_ssh_tunnel()
        print ("\n####### Test Ended #######\n")        

    def test_start_ssh_tunnel(self):
        print ("\ntest_get_next_ip_address\n")
        self.obj_ssh_tunnel_lib.start_ssh_tunnel(            
            "test_alias",
            "127.0.0.1",
            8080,
            "127.0.01",
            22,
            "testuser",
            "testuser",
            '127.0.0.1',
            0)

if __name__ == '__main__':
    unittest.main()