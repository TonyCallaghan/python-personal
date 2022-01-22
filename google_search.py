from googlesearch import search
query = "Jeffrey Epstein didn't kill himself?"
for i in search(query, start = 0, pause = 2):
	print(i)
