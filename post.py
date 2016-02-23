import facebook
token="CAAYGoBM5Q8gBACZCUh07FiZAH48Gjtj5FZAxgSKg6T38X75ZC49ZA5VRmZAMti9jJx5mklvlvI2C1PXR96Jbzop0QjXciprsRBKQ8xhb8dcbiVQIFjAyOr2LFtWTGJUwjzC4AEPzr4ZAFXl9mbKJMetVjZCOy2F5QUM32txyZAKZAZAZAGd2AyujqCgfZCOlDr8BpMF0VPEI9Ba1ayBTahj4ZCvGY6"
graph =facebook.GraphAPI(token)
PROFILE_ID ='me'
attach = {
  "name": 'Hello world',
  "link": 'http://www.google.com',
  "caption": 'test post',
  "description": 'some test',
  "picture" : 'download.jpg',
}

graph.put_wall_post('yap!!!!!!!!!!  Hello from Python ',profile_id = PROFILE_ID,attachment=attach )




#access token time extend 
'''https://graph.facebook.com/oauth/access_token?             
client_id=APP_ID&
client_secret=APP_SECRET&
grant_type=fb_exchange_token&
fb_exchange_token=EXISTING_ACCESS_TOKEN '''
