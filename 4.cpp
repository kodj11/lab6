#include <iostream>
#include <bitset>
#include <vector>
#include <string>

class NetAddress {
private:
    uint32_t address{ 0 };
    uint32_t netmask{ 0 };

    std::vector<uint8_t> split(std::string s, char delim) {
        std::vector<uint8_t> result;
        size_t pos = 0;
        while ((pos = s.find(delim)) != std::string::npos) {
            result.push_back(stoi(s.substr(0, pos)));
            s.erase(0, pos + 1);
        }
        result.push_back(stoi(s));
        return result;
    }

public:
    NetAddress(std::string ip, std::string mask) {

        auto ips = split(ip, '.');
        for (int i = 0; i < 4; ++i) {
            address |= (ips[i] << (i * 8));
        }

        auto masks = split(mask, '.');
        for (int i = 0; i < 4; ++i) {
            netmask |= (masks[i] << (i * 8));
        }
    }

    NetAddress(uint32_t address, uint32_t netmask)
        : address(address), netmask(netmask) {}

    NetAddress operator&(const NetAddress& other) const {
        return NetAddress(address & other.address, netmask & other.netmask);
    }

    bool operator==(const NetAddress& other) const {
        return address == other.address && netmask == other.netmask;
    }

    friend std::ostream& operator<<(std::ostream& os, const NetAddress& na);


};

std::ostream& operator<<(std::ostream& os, const NetAddress& na) {
    os << std::bitset<8>(na.address >> 24) << "."
        << std::bitset<8>(na.address >> 16) << "."
        << std::bitset<8>(na.address >> 8) << "."
        << std::bitset<8>(na.address) << "/"
        << std::bitset<32>(na.netmask);
    return os;
}

int main() {
    NetAddress ip("192.168.0.1", "255.255.255.0");
    NetAddress subnet = ip & ip;

    std::cout << "IP: " << ip << std::endl;
    std::cout << "Subnet: " << subnet << std::endl;

    std::cout << "('192.168.0.1', '255.255.255.0') == ('192.168.0.1', '255.255.255.0') ? -> " << (ip == ip) << std::endl;

    return 0;
}