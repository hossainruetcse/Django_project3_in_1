import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "eVn2thT0m67dUIsXBYBZhoanw",
    "consumer_secret"     : "FvjaE0sVdqbtuoVkGt1lytAMndIPQSbHwSmetwZG0ZNggvZisC",
    "access_token"        : "388776429-Jvb2gUnvp2AGF2jKGFSibWvhtBoX2gIqsO2Ohqrs",
    "access_token_secret" : "iXYdasIYYiKedZ1fw6mutHddOuiDF3VteAqjM9xd8IuGV" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
