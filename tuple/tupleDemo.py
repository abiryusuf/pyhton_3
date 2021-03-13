result = (1,23,20)

hours, mintues, seconds = result

print(hours, mintues, seconds)

# def file_size(file_info):
# 	name,type,size = file_info
# 	return("{:.2f}".format(size/1024))

# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21

# enumerate funtion
languages = ['Python', 'C', 'C++', 'Java']
i = 0
for c in languages:
    print(i, languages)
    i += 1

for i, language in enumerate(languages):
    print('{} - {}'.format(i + 1, language))


for x, y in enumerate(languages):
    print("{} - {}".format(x + 1, y))
