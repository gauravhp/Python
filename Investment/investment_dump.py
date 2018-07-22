import praw
import re

reddit = praw.Reddit(client_id='**************',
                     client_secret='***************************',
                     user_agent='***********')
with open('list_of_amc.txt') as f:
	amc_list=f.read().splitlines()

amc_dict = dict()

for amc in amc_list:
	amc_dict[amc] = 0

def main():
	f = open('mutualfunds.csv','w')
	investment_sub = reddit.subreddit("IndiaInvestments")
	for i in investment_sub.search("bi-weekly", limit=150):  #136
		i.comments.replace_more(limit=None)
		for comment in i.comments.list():
			for amc in amc_list:
				if amc.lower() in comment.body.lower():
					amc_dict[amc] = amc_dict[amc]+1
	for key,val in amc_dict.items():
		print(key, "=>", val)
		line = key +"," + str(val) +"\n"
		f.write(line)

	f.close()


if __name__ == '__main__':
	main()
