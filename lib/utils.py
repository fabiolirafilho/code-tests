def trim_str_stream(stream) -> str:
    return ( 
        str(stream) 
        .replace(' ', '')
        .replace('\t', '')
        .replace('\n', '')
    )