"""Basic pack file header loading test"""

from free_radical_pack import FreeRadicalPack


def read_pack_file(pack_file_path : str):
    """Reads a pack file and gets its header data."""
    test = FreeRadicalPack.from_file(pack_file_path)
    return test

def print_file_header(pack_file : FreeRadicalPack):
    """Prints pack file header information"""
    print("\nMagic:",pack_file.header.magic)
    print("File table offsets:",hex(pack_file.header.file_table_offset))
    print("File table count:",pack_file.header.file_table_count)
    print("Chunks Offset:",hex(pack_file.header.chunks_offset))
    print("Chunks Size:",hex(pack_file.header.chunks_size))
    print("Chunks Count:",pack_file.header.chunks_count)
    print("Seed:",pack_file.header.seed)

def print_first_file_entry(pack_file: FreeRadicalPack):
    """Prints data related to the first file in the pack file table."""
    #print(pack_file.file_table[0])
    for file in pack_file.file_table:
        if file.chunk_idx > 0:
            breakpoint()

def load_test(file_path : str) -> bool:
    """This loads a pack file and prints out some of its info."""
    pack_file = read_pack_file(file_path)
    if pack_file:
        print("\nPrinting out basic pack file stats:")
        print_file_header(pack_file)

        print("\nPrinting out basic pack file table entry stats:")
        print_first_file_entry(pack_file)
        return True
    else:
        print(f"\nCould not open {file_path}")
        return False


if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    _ = load_test("misc.pak")