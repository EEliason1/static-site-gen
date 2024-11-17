from textnode import TextNode

def main():
    testnode = TextNode("Test", "bold", "http://test.com")
    testrepr = testnode.__repr__
    print(testrepr)

main()