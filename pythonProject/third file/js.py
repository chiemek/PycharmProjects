import json

data = """
[{
"id" : "001",
"x" : "5",
"name" : "Paper"
},
{
"id" : "002",
"x" : "9",
"name" : "habeeb"
}

]
"""
info = json.loads(data)

print(info)