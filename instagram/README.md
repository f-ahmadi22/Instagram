# Instagram

# Description
This is a Django project aiming to replicate the functionality of Instagram, including user authentication, posting photos, following other users, direct messaging, and more.

# Install dependencies 
pip install -r requirements.txt

# Features
# Content App
    Manage posts, stories, and media content.
    Use Django admin interface for easy content management.

    Endpoints :
        create post :  'content/create-post/'
        create story :  'content/create-story/'
        Get all posts of followed users :  'content/posts/'
        mention a user in a story :  'content/mention/'
        get a story (view a story) : 'content/story/<int:pk>/'
        ** needs token authentication in every, so user needs to login
    


# Direct App
    Manage direct messaging via websocket connection. 

    Endpoints :
        Get all dialogs :  'direct/dialogs/'
        create connection : 'ws://localhost:8000/ws/chat/<dialog_id>/'


#  Log App
    Enable users to add items to their shopping cart.

    It only send logs when a post or story or a profile is viewed via signals in django.
    I used post_save signals.


# User activity App
    It manages user activities such as comment on a post and like an object(post, story, comment).

    Endpoints :
        add or delete comment : 'user-activity/comments/'
        like a post : 'user-activity/like-post/'
        like a story : 'user-activity/like-story/'
        like a comment : 'user-activity/like-comment/'



# User App
    For token authentication user needs to sign up and login to get token.
    It gets username and password fields.

    Endpoints :
        signup :  'user/signup/'
        login : 'user/login/'
        edit user profile : 'user/edit-profile/'
        view someone's profile : 'user/view-profile/<int:pk>/'
        follow someone : 'user/follow/'
        unfollow someone : 'user/unfollow/'
