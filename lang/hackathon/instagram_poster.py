import requests

image_url='https://i.postimg.cc/d11PMKdZ/Designer.jpg'

access_token='EAAGcry2OyuEBO2AFUZBNdMq3WXZCXJQUQfzeKZAac1gHmN0dpaw7CEq17p3R67774DSTvbrJgQoy5SESzPfiHZBRLemdfOTHq6bZAhi0Y7YdDIhxZCgaACulTkET8uJHySxaZCx4u6Yd2vOHoJkuZAqq4NmGm7iOjbDPzbEZAZCtVDv6oYHTnfxUQxBPeCEcdIlVnS'
api_version='v20.0'

ig_user_id=17841468053205975  #from facebook business manager settings you can find your insta account id 


def post_an_image_to_instagram(image_url, ig_user_id , access_token , caption= None ):
    api_version='v20.0' #might change with the developments in facebook, for now it is v20.0 

    #To post an image you need two steps! 

    #step one _____________________
    url = f'https://graph.facebook.com/{api_version}/{ig_user_id}/media'  # url we will use to make a request to post an image only in step 1
  
    params = {
        'image_url': image_url, #image should be running on the server ( lots of free websites doing that) + the format is jpeg only (  documentation stated that )
        'caption': caption,
        'access_token': access_token  #you can get it from facebook for developers --- ) tools --) generate token ( but give it the necessary permissions )
    }

    # Make the first POST request
    request_one=requests.post(url, params=params) 

    id = request_one.json()['id'] #their api returns us a special creation id that we will need to then post our image

    # step two _____________________

    # Construct the URL for the second step 
    url = f'https://graph.facebook.com/{api_version}/{ig_user_id}/media_publish'
    # Define the parameters
    params = {
        'creation_id': id,
        'access_token': access_token
    }

    # Make the POST request
    request_two=requests.post(url, params=params)
    
    return ' Success, the result from the first request:' , request_one.json(), 'the result from the second request:', request_two.json()

print( post_an_image_to_instagram(image_url, ig_user_id , access_token , 'My first automatic post in instagram!'))
