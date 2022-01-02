items = list()

filename = 'Nouns/Animals_Unsorted.txt'
with open (filename) as file_in:
	for line in file_in:				# For every line in Animals.txt
		items.append(line.strip()) 		# Add to 'items' list and remove \n character

items = list(dict.fromkeys(items))  	# Remove duplicates
items.sort()							# Sort it alphabetically
for i in range(len(items)):			
    items[i] = items[i].lower()			# Lower case everything

filename = 'Nouns/Animals.txt'	# Open new file 
with open (filename, 'w') as file_out:	
	for item in items:
		file_out.write(item + '\n')		# Store sorted list in new file
