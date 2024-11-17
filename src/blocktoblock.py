def block_to_block_type(block: str) -> str:
    block = block.strip()
    
    if not block:
        return 'paragraph'
    
    if block.startswith('# '):
        return 'heading'
    
    if block.startswith('```') and block.endswith('```'):
        return 'code'
    
    if all(line.startswith('> ') for line in block.splitlines()):
        return 'quote'
    
    if all(line.lstrip().startswith(('* ', '- ')) for line in block.splitlines()):
        return 'unordered_list'
    
    if all(line.lstrip().startswith(f'{i+1}. ') for i, line in enumerate(block.splitlines())):
        return 'ordered_list'
    
    return 'paragraph'
