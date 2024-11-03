import fileinput

class Packet:
    def __init__(self, version, type_id, sub_packets, literal=None):
        self.version = version
        self.type_id = type_id
        self.literal = literal
        self.sub_packets = sub_packets

def read_chunk(packet, chunk_len):
    return packet[:chunk_len], packet[chunk_len:]

def parse(packet):
    
    version, type_id, packet = int(packet[:3], 2), int(packet[3:6], 2), packet[6:]
    if type_id == 4:
        literal = ''
        while True:
            chunk, packet = read_chunk(packet, 5)
            literal += chunk[1:]
            if chunk[0] == '0':
                break
        parsed_packet = Packet(version, type_id, [], int(literal, 2))
    else:
        len_id, packet = int(packet[0], 2), packet[1:]
        sub_packets = []
        if len_id == 0:
            chunk, packet = read_chunk(packet, 15)
            sub_packet_len = int(chunk, 2)
            sub_packet, packet = read_chunk(packet, sub_packet_len)
            while len(sub_packet) > 6:
                p, sub_packet = parse(sub_packet)
                sub_packets.append(p)
            parsed_packet = Packet(version, type_id, sub_packets)
        if len_id == 1:
            chunk, packet = read_chunk(packet, 11)
            num_sub_packets = int(chunk, 2)
            for _ in range(num_sub_packets):
                p, packet = parse(packet)
                sub_packets.append(p)
            parsed_packet = Packet(version, type_id, sub_packets)
    
    return parsed_packet, packet
        
import functools

def pt1(packet):
    return packet.version + sum(pt1(p) for p in packet.sub_packets)

def pt2(packet):
    match packet.type_id:
        case 0:
            return sum(pt2(p) for p in packet.sub_packets)
        case 1:
            return functools.reduce(lambda a, b: a * b, [pt2(p) for p in packet.sub_packets], 1)
        case 2:
            return min(pt2(p) for p in packet.sub_packets)
        case 3:
            return max(pt2(p) for p in packet.sub_packets)
        case 4:
            return packet.literal
        case 5:
            return int(pt2(packet.sub_packets[0]) > pt2(packet.sub_packets[1]))
        case 6:
            return int(pt2(packet.sub_packets[0]) < pt2(packet.sub_packets[1]))
        case 7:
            return int(pt2(packet.sub_packets[0]) == pt2(packet.sub_packets[1]))
        case _:
            raise Exception("Bad type id")

s = next(fileinput.input()).strip()
packet = [bin(int(ch, 16))[2:].zfill(4) for ch in s.split()][0].zfill(len(s) * 4)
p, _ = parse(packet)    

print(pt1(p), pt2(p))
