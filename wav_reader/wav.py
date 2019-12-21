import numpy as np


class Wav:
    def __init__(self, file_path):
        self._file = file_path
        self._channels_count = 0
        self._bytes = []
        self._size = 0
        self._byteRate = 0

    def get_bytes(self):
        return self._bytes

    def read(self):
        with open(self._file, "rb") as f:
            chunk_id = f.read(4)
            file_size = f.read(4)
            riff_type = f.read(4)

            fmt_id = f.read(4)
            fmt_size = f.read(4)
            fmt_code = f.read(2)
            self._channels_count = f.read(2)
            sample_rate = f.read(4)
            self._byteRate = f.read(4)
            fmt_block_align = f.read(2)
            bit_depth = int.from_bytes(f.read(2), "little")

            if fmt_size == 18:
                fmt_extra = f.read(2)
                f.read(int.from_bytes(fmt_extra, "little"))

            data_id = f.read(4)
            bytes = f.read(4)

            byte_array = f.read(int.from_bytes(bytes, "little") // 8)

            bytes_for_samp = bit_depth / 8
            samps = int.from_bytes(bytes, "little") / bytes_for_samp

            self._byteRate = bit_depth

            if bit_depth == 64:
                self._bytes = np.array([v for v in byte_array], dtype=np.int64)
            elif bit_depth == 32:
                self._bytes = np.array([v for v in byte_array], dtype=np.int32)
            elif bit_depth == 16:
                self._bytes = np.array([v for v in byte_array], dtype=np.int16)
            else:
                raise Exception("Bit rate not found...")
