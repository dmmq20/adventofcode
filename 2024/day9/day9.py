import fileinput
from copy import deepcopy


class BlockwiseCompaction:
    def compact(self, files):
        for i in range(len(files) - 1, -1, -1):
            current_file = files[i]
            for j in range(i):
                files[j].store_blocks(current_file)
                if current_file.file_len == 0:
                    break


class WholeFileCompaction:
    def compact(self, files):
        for i in range(len(files) - 1, -1, -1):
            current_file = files[i]
            for j in range(i):
                if files[j].store_whole_file(current_file):
                    break


class Disk:
    def __init__(self, disk_map):
        self.files = self._parse(disk_map)

    def _parse(self, disk_map):
        files = []
        for i in range(0, len(disk_map), 2):
            f = File(len(files), *disk_map[i:i+2])
            files.append(f)
        return files

    def compact(self, strategy):
        new_storage = Disk([])
        new_storage.files = deepcopy(self.files)
        strategy.compact(new_storage.files)
        return new_storage

    def checksum(self, include_empty=False):
        storage = []
        for f in self.files:
            if not include_empty:
                storage.extend(block for block in f.chunk if block is not None)
            else:
                storage.extend(f.chunk)

        return sum(i * block for i, block in enumerate(storage) if block is not None)


class File:
    def __init__(self, _id, file_len, free=0):
        self.chunk = [_id] * file_len + [None] * free
        self.free = free
        self.file_len = file_len
        self.ptr = file_len
        self.idx = 0

    def store_blocks(self, f):
        if not self.free:
            return False
        blocks_to_copy = min(self.free, f.file_len)
        for _ in range(blocks_to_copy):
            self.chunk[self.ptr] = f.chunk[f.idx]
            f.chunk[f.idx] = None
            self.ptr += 1
            self.free -= 1
            f.idx += 1
            f.file_len -= 1

        return self.free

    def store_whole_file(self, f):
        if self.free < f.file_len:
            return False
        for i in range(f.file_len):
            self.chunk[self.ptr + i] = f.chunk[i]
            f.chunk[i] = None
        self.free -= f.file_len
        self.ptr += f.file_len
        f.free += f.file_len
        f.file_len = 0
        f.ptr = 0

        return True


data = [int(n) for n in "".join(fileinput.input()).strip()]
disk = Disk(data)
blockwise_result = disk.compact(BlockwiseCompaction())
wholefile_result = disk.compact(WholeFileCompaction())

print(f"Part 1: {blockwise_result.checksum()}")
print(f"Part 2: {wholefile_result.checksum(include_empty=True)}")
