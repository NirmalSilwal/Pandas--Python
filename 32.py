from lxml import objectify
path = 'D:\\datascience\\python\\pandas\\1.xml'
parsed = objectify.parse(open(path))
print(parsed)
root = parsed.getroot()
data = []
print(root)
print(root.INDICATOR_SEQ)

