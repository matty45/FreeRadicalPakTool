meta:
  id: free_radical_pack
  file-extension: pak,qik
  endian: be
  title: Free Radical Engine Pack file format that is used in the cancelled Battlefront games and Haze.
  
seq:
  - id: header
    type: pak_header
    
instances:
  file_table:
    pos: header.file_table_offset
    type: file_entry
    repeat: expr
    repeat-expr: header.file_table_count
    
types:
  pak_header:
    seq:
      - id: magic
        contents: 'PBCK'
      - id: file_table_offset
        type: u4
      - id: file_table_count
        type: u4
      - id: chunks_offset
        type: u4
      - id: chunks_size
        type: u4
      - id: chunks_count
        type: u2
        doc: Amount of chunks the pak file has been split into. e.g misc.pak.00
      - id: seed
        type: u2
        
  file_entry:
    seq:
      - id: crc
        type: u4
      - id: size
        type: u4
      - id: compressed_size
        type: u4
      - id: offset
        type: u4
      - id: chunk_idx
        type: u1
      - id: pak_num
        type: u1
      - id: pad
        type: u2