# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class FreeRadicalPack(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = FreeRadicalPack.PakHeader(self._io, self, self._root)
        self.file_table = []
        for i in range(self.header.file_table_count):
            self.file_table.append(FreeRadicalPack.FileEntry(self._io, self, self._root))


    class PakHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x50\x42\x43\x4B":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x42\x43\x4B", self.magic, self._io, u"/types/pak_header/seq/0")
            self.file_table_offset = self._io.read_u4be()
            self.file_table_count = self._io.read_u4be()
            self.chunks_offset = self._io.read_u4be()
            self.chunks_size = self._io.read_u4be()
            self.chunks_count = self._io.read_u2be()
            self.seed = self._io.read_u2be()


    class FileEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.crc = self._io.read_u4be()
            self.size = self._io.read_u4be()
            self.compressed_size = self._io.read_u4be()
            self.offset = self._io.read_u4be()
            self.chunk_idx = self._io.read_bits_int_be(3)
            self._io.align_to_byte()
            self.pak_num = self._io.read_u1()



