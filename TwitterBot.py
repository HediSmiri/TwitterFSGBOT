#!/usr/bin/python3

import os,sys
import tweepy

# -*- coding: utf-8 -*-

# Clear cmd or Terminnal befor Lunching the script
os.system('cls' if os.name == 'nt' else 'clear')

class TwitterBotFSG:
    # Private Attribute For Security Reason 
    # Change Your ApI Here For Your Account API
    _bearer_token = "%2BNMZGOgJz7PyCXz0O9ZkauJoY%"
    
    _consumer_key ="e2xOuOUbUCjeAriyNn7wq6KMw"
    _consumer_secret=""
    _access_token="3315000556-"
    _access_token_secret=""

    # Make a Connection Using API if Any Error The Script Lunch A Exception
    def Connect(self):
        try:
            client = tweepy.Client(
                                bearer_token=self._bearer_token, 
                                consumer_key=self._consumer_key,
                                consumer_secret=self._consumer_secret, 
                                access_token=self._access_token, 
                                access_token_secret=self._access_token_secret
                                )
            self.client = client
        except Exception :
            print("Connection Error ... Check Your API")
            sys.argv[0]
    
    # You Can Write a Message For tweet in twetter 
    def Make_tweet(self,tweet):
        try:
            self.client.create_tweet(text=tweet)
            print("ALL is Done .")
        except Exception as e:
            print("Somthing Error "+e)
    
    # You Can Make a search for recent tweet Using a Hashtag 
    def SearchTweeterTweet(self,q):
        recent = []
        searchResult = self.client.search_recent_tweets(q)
        for search in searchResult:
            recent.append(search)
        return recent

    def DeleteTweet(self,id):
        try:
            self.client.delete_tweet(id)
            print("Done .")
        except:
            print("Somthing Error ... ")


    # This is the Banner i use it Like a static Methode 
    @staticmethod
    def banner():
        print("""
###################################################################################

 _____          _ _   _            _____ ____   ____ ____   ___ _____ 
|_   _|_      _(_) |_| |_ ___ _ __|  ___/ ___| / ___| __ ) / _ \_   _|
  | | \ \ /\ / / | __| __/ _ \ '__| |_  \___ \| |  _|  _ \| | | || |  
  | |  \ V  V /| | |_| ||  __/ |  |  _|  ___) | |_| | |_) | |_| || |  
  |_|   \_/\_/ |_|\__|\__\___|_|  |_|   |____/ \____|____/ \___/ |_|
                                  Created By Hedi_Smiri

###################################################################################

         [+]- This Project Designed For Education Purpose -[+]
         [+]- TwitterFSGProject Using Twitter API v2 -[+]
         [+]- This Bot Can Tweet Search Delate Tweet -[+]
         [+]- Open Source Project U Can Add Some Functionality to It -[+]

###################################################################################

        [1] - Make a tweet Using Your API
        [2] - Make a Search in Twetter
        [3] - Delete Your Tweet
        [4] - Exit 

        """)


def main():
    TwitterBotFSG.banner()
    try:
        choice = int(input("[+] - choice : "))
    except:
        print("Your Input Must Be From 1 - 4 Try again ...")
        sys.exit(0)
    # Instance of My Class TwitterBotFSG
    Bot = TwitterBotFSG()
    Bot.Connect() # Make a Connection Using the API
    if choice == 1 :
        tweet = input("Enter Your Tweet Here : ")
        Bot.Make_tweet(tweet)
        
    elif choice == 2 :
        querySearch = input("Enter Your Hashtag or Word for Search : ")
        resut = Bot.SearchTweeterTweet(querySearch)
        for tweet in resut:
            print(tweet,"\n")
    elif choice == 3 :
        try:
            id = int(input("Enter The id Of twwet that you want to delete :  "))
        except:
            print("Id Must Be Numbers Not String ")
        Bot.DeleteTweet(id)
    elif choice == 4 :
        print("\nThanks For Using This Script ^_^ Bye\n")
        sys.exit(0)

if __name__ =="__main__":
    try:
        while True :
            main()
    except :
        print("Connection Error ...")