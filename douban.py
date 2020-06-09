import requests
from bs4 import BeautifulSoup
from movie import Movie


movie_lst = []
start = 0
cnt = 0

while start < 100:


	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'	
	}

	url = 'https://movie.douban.com/top250?start='+str(start)+'&filter='

	r = requests.get(url, headers=headers)
	#print(r.status_code)


	soup = BeautifulSoup(r.content,'lxml')
	#print(soup.prettify())

	infos = soup.find_all('div','info')

	for i in infos:

		new = Movie()
		name = i.find('span','title').string

		new.name = name
		
		bd_div = i.find('div','bd')
		score_tag = bd_div.find('span','rating_num').string

		new.score = score_tag

		#print(score_tag)
		quote_tag = bd_div.find('span','inq')

		if quote_tag != None:
			#print(quote_tag.string)
			new.quote = quote_tag.string
		
		movie_lst.append(new)

		
	start += 25


for movie in movie_lst:
	print(movie.name + ': '+movie.score+'\n')
	print('----'+movie.quote+'----\n')
	print('\n')