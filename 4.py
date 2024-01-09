
class NetAddress:
    def __init__(self, ip, mask):
        self.address = self._parse_ip(ip)
        self.netmask = self._parse_mask(mask)

    def __and__(self, other):
        return NetAddress(self.address & other.address, 
                          self.netmask & other.netmask)
                          
    def __eq__(self, other):
        return self.address == other.address and self.netmask == other.netmask

    def _parse_ip(self, ip):
        return sum(int(x) << (i * 8) for i, x in enumerate(ip.split('.')))
    
    def _parse_mask(self, mask):
        return sum(int(x) << (i * 8) for i, x in enumerate(mask.split('.')))
        
    def __str__(self):
        return f"{self._int_to_ip(self.address)}/{self._int_to_mask(self.netmask)}"

    def _int_to_ip(self, addr):
        return '.'.join(str(addr >> (i * 8) & 0xff) for i in range(3,-1,-1))

    def _int_to_mask(self, mask):
        return '.'.join(str(mask >> (i * 8) & 0xff) for i in range(3,-1,-1))

    def get_network_address(self):
        network_addr = self.address & self.netmask
        return f"{network_addr&0xFF}.{(network_addr>>8)&0xFF}.{(network_addr>>16)&0xFF}.{(network_addr>>24)&0xFF}"

ip = NetAddress("192.168.0.1", "255.255.255.0")
subnet = ip.get_network_address()

print(f"IP: {ip}")
print(f"Subnet: {subnet}")
print(f"ip == ip ? -> {(ip==ip)}")
