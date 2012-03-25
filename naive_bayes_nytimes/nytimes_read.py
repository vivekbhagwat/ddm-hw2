import urllib2
import json
import csv
import time

def get_articles(api_key):
	sections = ("Arts", "Business", "Obituaries", "Sports", "World")

	for sect in sections:
		article_count = 0
		offset = 0
		f = open(sect+'.tsv', 'w')
		# writer = csv.writer(open(sect+'.tsv', 'w'), delimiter="\t")
		print "Starting " + sect

		while article_count < 2000:
			print "Have written " + str(article_count)

			#for nytimes QPS limit of 10
			if offset % 10 == 0:
				time.sleep(1)

			url2 = 'http://api.nytimes.com/svc/search/v1/article?format=json&query=nytd_section_facet:['
			url2 += sect+']&rank=newest&api-key='+api_key+'&offset='+str(offset)

			response = json.loads(urllib2.urlopen(url2).read())
			offset = int(response['offset']) + 1

			article_count += len(response['results'])

			for result in response['results']:
				if result.has_key('body'):
					# writer.writerow(result['url'].encode('ascii', 'ignore'))
					# writer.writerow(result['title'].encode('ascii', 'ignore'))
					# writer.writerow(result['body'].encode('ascii', 'ignore'))

					f.write(result['url'].encode('ascii', 'ignore') + "\t")
					f.write(result['title'].encode('ascii', 'ignore') + "\t")
					f.write(result['body'].encode('ascii', 'ignore') + "\n")
				else:
					article_count -= 1

		f.close()



# api_key = '15e447cd50a25d21583ff2600d856d84:2:56161638' #bhagwat.vivek@gmail.com
api_key = '1bb3d924efb26a1c01379c5bb5994e91:15:65865489' #vivek@vivekbhagwat.com
get_articles(api_key)

