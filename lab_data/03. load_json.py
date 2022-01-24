import json

f = open("../data/labels/labels.json")
label = json.load(f)

print(label)
print(type(label))
print(len(label))

print(label[0])
print(type(label[0]))

print(label[0].keys())
print(label[0]['attributes'])

print(label[0]['labels'])

print(label[0]['labels'][0]['box2d'])

x1 = (label[0]['labels'][0]['box2d']['x1'])
y1 = (label[0]['labels'][0]['box2d']['y1'])
x2 = (label[0]['labels'][0]['box2d']['x2'])
y2 = (label[0]['labels'][0]['box2d']['y2'])

print(x1, y1, x2, y2)