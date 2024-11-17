import re

def markdown_to_blocks(markdown):
    blocks = []
    raw_blocks = re.split(r'\n\s*\n', markdown.strip())

    for block in raw_blocks:
        block = block.strip()
        
        if not block:
            continue
        
        if block.startswith('```') and block.endswith('```'):
            block_content = block.strip('```').strip()
            blocks.append(f'```\n{block_content}\n```')
        else:
            block = re.sub(r'`(.*?)`', r'`\1`', block)
            blocks.append(block)
    
    return blocks
