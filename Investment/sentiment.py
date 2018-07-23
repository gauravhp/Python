import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


reddit = praw.Reddit(client_id='**************',
                     client_secret='***************************',
                     user_agent='***********')

analyser = SentimentIntensityAnalyzer()

with open('list_of_amc.txt') as f:
	amc_list=f.read().splitlines()

amc_dict = dict()

for amc in amc_list:
	amc_dict[amc] = (0,0)

def main():
	f = open('mutualfunds.csv','w')
	f.write("Fund Name, Mention Count, Sentiment\n")
	investment_sub = reddit.subreddit("IndiaInvestments")
	for i in investment_sub.search("bi-weekly", limit=200):  #136
		i.comments.replace_more(limit=None)
		for comment in i.comments.list():
			for amc in amc_list:
				if amc.lower() in comment.body.lower():
					senti=analyser.polarity_scores(comment.body)
					tup = amc_dict[amc]
					lst = list(tup)
					lst[0] = lst[0]+1
					lst[1] = (lst[1]+senti['compound'])/2
					amc_dict[amc]=tuple(lst)
	for key,val in amc_dict.items():
		print(key, "=>", val)
		line = key +"," + str(val[0])  + "," + str(val[1]) +"\n"
		f.write(line)

	f.close()


if __name__ == '__main__':
	main()
