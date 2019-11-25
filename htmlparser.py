# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
link = "index.html"

for x in range(0,10):

		with open(link+str(x)) as fp:
   				soup = BeautifulSoup(fp)
   					soup.find_all("title")

						# [<title>The Dormouse's story</title>]
						and
							with open('proxylist.txt', 'w') as f:
								print.f(soup.find_all("title"))

else
return= 1
