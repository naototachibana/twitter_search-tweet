import json
import config
from requests_oauthlib import OAuth1Session
import argparse


def parse_arguments():

    
    # Set up the argument parser.
    parser = argparse.ArgumentParser(description='help message of this parser')
    
    choise_list = ['hoge', 'huga']
    parser.add_argument('--method', '-m', type=str, choices=choise_list,
                        help='chosen method', default='hoge')
                        
    parser.add_argument('--label', '-l', nargs='+',
                        default=['value1', 'value2'],
                        help='labels')

    parser.add_argument('--query', '-q', type=str,
                        help='search query of tweets', default='hoge')

    return parser.parse_args()

def main():
    args = parse_arguments()
    # OAuth authentication
    CK      = config.CONSUMER_KEY
    CS      = config.CONSUMER_SECRET
    AT      = config.ACCESS_TOKEN
    ATS     = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)

    # Endpoint url
    url = 'https://api.twitter.com/1.1/search/tweets.json'


    query_keyword = args.query
    num_tweets = 10
    params ={
            'count' : num_tweets,
            'q'     : query_keyword
            }

    req = twitter.get(url, params = params)

    if req.status_code == 200:
        res = json.loads(req.text)
        for line in res['statuses']:
            print(line['text'])
            print('*******************************************')
    else:
        print("Failed: %d" % req.status_code)
