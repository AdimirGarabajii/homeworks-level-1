from os import system

#text = text_lines + text_lines1 + text_lines2

text_lines = [
    'Python is a high-level, interpreted, general-purpose programming ',
    'language. Its design philosophy emphasizes code readability with the use ',
    'of significant indentation.'
]
text_lines.append(input())
text_lines.append(input())

system('cls')

for line in text_lines:
    print(line)
#for i in range(len(text_lines)):
    #print(i,text_lines[i])
#print('',text_lines[0],'\n', text_lines[1])
#print(text_lines[1])
#print(text_lines[2])

print()