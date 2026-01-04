# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class FreeRadicalPack(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(FreeRadicalPack, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.header = FreeRadicalPack.PakHeader(self._io, self, self._root)


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _ = self.file_table
        if hasattr(self, '_m_file_table'):
            pass
            for i in range(len(self._m_file_table)):
                pass
                self._m_file_table[i]._fetch_instances()



    class FileEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(FreeRadicalPack.FileEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.crc = self._io.read_u4be()
            self.size = self._io.read_u4be()
            self.compressed_size = self._io.read_u4be()
            self.offset = self._io.read_u4be()
            self.chunk_idx = self._io.read_u1()
            self.pak_num = self._io.read_u1()
            self.pad = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class PakHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(FreeRadicalPack.PakHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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


        def _fetch_instances(self):
            pass


    @property
    def file_table(self):
        if hasattr(self, '_m_file_table'):
            return self._m_file_table

        _pos = self._io.pos()
        self._io.seek(self.header.file_table_offset)
        self._m_file_table = []
        for i in range(self.header.file_table_count):
            self._m_file_table.append(FreeRadicalPack.FileEntry(self._io, self, self._root))

        self._io.seek(_pos)
        return getattr(self, '_m_file_table', None)


