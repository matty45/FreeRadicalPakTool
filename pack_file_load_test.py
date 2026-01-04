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

def validate_file_entries(pack_file: FreeRadicalPack):
    """Validates all file entries in the pak."""
    
    if len(pack_file.file_table) != len(set(pack_file.file_table)):
        print("Duplicate entries detected in the file table!")
        return False

    for file in pack_file.file_table:
        if file.chunk_idx > pack_file.header.chunks_count:
            print(f"File {file.pak_num} has a chunk index bigger than the total chunk count {pack_file.header.chunks_count} inside of the main header.")
            return False
        
        if file.compressed_size > file.size:
            print(f"File {file.pak_num} has broken compression!")
            return False
        

            
def load_test(file_path : str) -> bool:
    """This loads a pack file and prints out some of its info."""
    pack_file = read_pack_file(file_path)
    if pack_file:
        print("\nPrinting out basic pack file stats:")
        print_file_header(pack_file)

        print("\nValidating File Entries:")
        validate_file_entries(pack_file)
        return True
    else:
        print(f"\nCould not open {file_path}")
        return False


if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    _ = load_test("misc.pak")