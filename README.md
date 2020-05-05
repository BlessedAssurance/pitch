# Pitch

## Author

- Kirui Vincent

## Description of the Project

- This is an web app that allows a user to sign in/up and post a one minute pitch/es and also to upvote and downvote on different pitches or comment.

## USER Story

- Comment on the different pitches posted py other users.
- See the pitches posted by other users.
- Vote on s pitch they have viewed by giving it a upvote or a downvote.
- Register to be allowed to log in to the application
- View pitches from the different categories.
- Submit a pitch to a specific category of their choice.

# BDD 

- | Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | *Page Loads on browser* | Get all posts, select between signup and login |
| Select signup | *Email, Username, Password* | Redirect to login |
| Select Login | *Username and Password* | Redirect to ap pitches based on categories |
| Select comment button | *Comment* | Load Form that you input comment |
| Click on submit |  | Redirect to all comments template with your comment and other comments |

## Development Installation 

1. Cloning the repo:

https://github.com/kiprotichdominic/Moringa-Project-Pitch

2. Move to the folder and install requirements

    cd pitch-world
    pip install -r requirements.txt

3. Exporting Configurations

    export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

4. Running the application

    python3.6 manage.py server

5. Testing the application

 python3.6 manage.py test

Open the application on your browser 127.0.0.1:5000.

## Technology used
- Python3.6
- Flask
- Heroku

## Contact Information

- @ engineervinceblair@gmail.com 

## License
- *MIT* License