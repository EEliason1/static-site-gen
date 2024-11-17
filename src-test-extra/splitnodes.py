from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text == "":
            new_nodes.append(TextNode("", TextType.NORMAL))
            continue

        parts = node.text.split(delimiter)

        if len(parts) == 1:
            new_nodes.append(node)
            continue

        for i, part in enumerate(parts):
            if part:
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(part, text_type))

    return new_nodes if new_nodes else [TextNode("", TextType.NORMAL)]

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        if node.text_type == TextType.NORMAL:
            images = extract_markdown_images(text)
            if images:
                last_index = 0
                for alt_text, url in images:
                    sections = text.split(f"![{alt_text}]({url})", 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                    text = sections[1]
                if text:
                    new_nodes.append(TextNode(text, TextType.NORMAL))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        if node.text_type == TextType.NORMAL:
            links = extract_markdown_links(text)
            if links:
                last_index = 0
                for anchor_text, url in links:
                    sections = text.split(f"[{anchor_text}]({url})", 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
                    text = sections[1]
                if text:
                    new_nodes.append(TextNode(text, TextType.NORMAL))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    
    nodes = split_nodes_image(nodes)
    
    nodes = split_nodes_link(nodes)
    
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '*', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    
    return nodes

