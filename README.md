#### Application authorization

GET request to join.agiliq.com/oauth/authorize?client_id=client_id&redirect_uri=redirect_uri to get 
redirect_uri?code=code

#### Token Exchange

exchange_token.py returned u'{"access_token": "access_token", "token_type": "simple"}'

#### POST resume

post_resume.py