from wordnik import *
import random
import twitter

api = twitter.Api(consumer_key='TWITTER_KEY', consumer_secret="TWITTER_SECRET", access_token_key='TWITTER_ACCESS_TOKEN', access_token_secret="TWITTER_TOKEN_SECRET")

apiUrl = "http://api.wordnik.com/v4"
apiKey = "WORDNIK_API_KEY"
client = swagger.ApiClient(apiKey, apiUrl)
WordsApi = WordsApi.WordsApi(client)

adjectives = WordsApi.getRandomWords(includePartOfSpeech='adjective', limit=10)
nouns = WordsApi.getRandomWords(includePartOfSpeech='noun', limit=10)

slogans = ["Make America " + adjectives[2].word + " again!!",  nouns[2].word.capitalize() + " we can believe in!!", nouns[2].word.capitalize() + "-time in America!!!", "A " + nouns[2].word + " in every pot!!", "A " + adjectives[2].word + " deal for America!!"] 
slogan = random.choice(slogans)

status = api.PostUpdate(adjectives[0].word.capitalize() + " " + nouns[0].word.capitalize() + "/" + adjectives[1].word.capitalize() + " " + nouns[1].word.capitalize() + " 2016: " + slogan)
print status.text
