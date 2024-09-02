'''
planet1 = "Closest to the Sun"

print(planet1)

print(planet1[1])
print(planet1[2])
print(planet1[-1])

# slicing string
print(planet1[1:4])
print(planet1[:7])

# slicing tuple
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[1])
print(devops[4])
print(devops[-1])
print(devops[2 : -1])
print(devops[2 : -1][2])
print(devops[2 : -1][2][1:8])
'''

# Dictionary Example
Skills = {
    "DevOps": ('AWS', "Jenkins", 'Python', "Ansible"),
    "Development": ["Java", "NodeJs", ".net"]
}

print(Skills)
print(Skills["DevOps"])
print(Skills["Development"])
print(Skills["DevOps"][-1])
print(Skills["DevOps"][-1][:3])





