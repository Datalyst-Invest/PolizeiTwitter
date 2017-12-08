import pandas as pd;
import re;
import matplotlib.pyplot as plt



#A dictionary with days as keys and lists of hashtags as values
all_hashtags_dict = {}
#Importing excel file
d = pd.read_csv('/Users/david/PycharmProjects/PolizeiTwitter/polizeiberlin_tweets.csv')
#Creating pandas DataFrame from Excel file
df = pd.DataFrame(d)
#Pushing all tweets into a list
tweets = df['text'].tolist()

for el in tweets:
    #All hashtags in one tweet el
    hashtag_list = re.findall(r"#(\w+)", el)
    #Sorting the hashtaglist to get
    hashtag_list.sort()
    hashtag_list = [x.lower() for x in hashtag_list]
    #Pushing all hashtags in a common set
    for hashtag in hashtag_list:
        if hashtag not in all_hashtags_dict:
            all_hashtags_dict[hashtag] = 1
        else:
            all_hashtags_dict[hashtag] = all_hashtags_dict[hashtag] + 1


