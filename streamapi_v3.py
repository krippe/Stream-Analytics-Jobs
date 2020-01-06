# -*- coding: utf-8 -*-
from twython import TwythonStreamer
import config
import json
from  azure.servicebus import ServiceBusService
import re

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        sbs = ServiceBusService(config.a_event_hub_namespace, shared_access_key_name = config.a_shared_access_key_name, shared_access_key_value = config.a_shared_access_key_value)
        D = {}

        if 'text' in data:
            D["timestamp"] = data['timestamp_ms']
            D["tweet_id"] = data['id_str']
            D["user_id"] = data['user']['id_str']
            D["screen_name"] = data['user']['screen_name']

            if data['truncated'] is True:                
                D["tweet"] = re.sub("'", "|", data['extended_tweet']['full_text'])
            else:
                D["tweet"] = re.sub("'", "|", data['text'])

            D["retweeted_id"] = ''
            D["retweeted_user_id"] = ''
            D["retweet"] = 0

            if 'retweeted_status' in data:
                D["retweeted_id"] =  data['retweeted_status']['id_str']
                D["retweeted_user_id"] = data['retweeted_status']['user']['id_str']
                D["retweet"] = 1

            list = ''
            for lists in data['entities']['hashtags']:
                list = list + lists['text'] + ' '

            D["hashtags"] = list

            print (data['timestamp_ms'])
            sbs.send_event("twitterstreamin", json.dumps(D,ensure_ascii=False).encode('utf8'))

        else:
            for key, value in data.items():
                print (key, ' : ', value)   

        return True

    def on_error(self, status_code, data):
        print (status_code + 'hej')
        time.sleep(60)
        return True

    def on_timeout(self):
        print ('Time out')
        return True

def streamed():
    while True:
        try:
            stream = MyStreamer(config.app_key, config.app_secret, config.oauth_token, config.oauth_token_secret)
            stream.statuses.filter(language='sv', track='och, att, det, som, på, är, av, för, med, till, den, har, inte, om, ett, han, men, var, jag, sig, från, vi, så, kan, nu, du, var, här, när, ska, vad, mig, från')
        except:
            continue

streamed()
