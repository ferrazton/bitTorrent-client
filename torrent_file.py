import math

class TorrentFile:
    def __init__(self, t_all):
        self.t_all = t_all
        self.t_announce = self.t_all[b'announce'].decode('utf-8')
        self.t_info = self.t_all[b'info']
        self.t_piece_length = self.t_info[b'piece length']
        self.t_files = self.t_info[b'files']
        self.t_total_size = 0
        for file_ in self.t_files:
            self.t_total_size += file_[b'length']
    
    def print_all_info(self):
        print(f"\nIDENTIFIED {len(self.t_files)} FILES:\n")
        for file_ in self.t_files:
            print(f"PATH: {file_[b'path']}")
            print(f"LENGTH: {file_[b'length']} BYTES\n")
        print(f"PIECE LENGTH: {self.t_piece_length}")
        print(f"TOTAL LENGTH: {self.t_total_size}")
        print(f"PIECES: {math.ceil(self.t_total_size/self.t_piece_length)}\n")