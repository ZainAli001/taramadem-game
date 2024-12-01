from flask import Flask, render_template, request

app = Flask(__name__)
# Define game stages and their associated results and images
game_data = {
    "start": {
        "text": "You are on an alien planet. What will you do next?",
        "image": "img/TARAMADEM_2_surface_spaceship-1.jpg",
    },
    "explore": {
        "text": "You discover a mysterious crater. What now?",
        "image": "img/TARAMADEM_3_spider-1.jpg",
    },
    "default": {
        "text": "Welcome to the TARAMADEM Game!",
        "image": "img/one.jpeg",
    },
}
def statements():
    return '''
<p>1. You have landed on an unknown planet while travelling across space and it appears that a key is required to get your spaceship turned back on.</p>
<p>2. After landing on the planet, you inspect your pockets and find matches and a rope.</p>
<p>3. Shortly after landing, you hear someone yelling for help and you see someone down in a huge crater.</p>
<p>4. Next to the crater there is a large tree that looks stable enough to tie a rope around and climb down.</p>

<p>What would you like to do next? (climb down, use the rope, help, or escape)</p>
    '''
# Game logic functions
def world(choice):

    if choice == "climb down" or choice == "use the rope" or choice == "help":
        return spiderroom("")
    elif choice == "escape":
        return goodbye("") #works fine
    else:
        print("world invalid")
        print("Invalid choice. Try again.")
        return world()
# def goodbye():
#   print(" You are now free to traverse space solitarily, bye friend.")
 
def spiderroom_statements():
    
    return '''
        <p>1. You tie your rope around the tree and rappel down.</p>
        <p>2. You are now in a room with a giant spider. There is a key on the spider's web.</p>
        <p>3. The spider is on the left side of the room and the key is on the right side of the room.</p>
        <p>4. There is also a door, next to the key.</p>
        <p><strong>Do you fight the spider or grab the key and go through the door? (F/G)</strong></p>

        ''' 
def spiderroom(choice=None):
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_3_spider-1.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''

    room_text = spiderroom_statements()  # Get the statements
    if not choice:
        return room_text + background_script # Show the text first
    if choice == "f":
        return '''You were badly damaged by the spider and can no longer go down and help your friend.''' + "<br>" + goodbye("")

    elif choice == "g":
        return friendwoot("")
    else:
        return render_template("home.html", result=room_text + "\nInvalid choice. Try again.")
def friendwoot_statements():
    return '''
<p>1. You got the key and you go to the next room.</p>
<p>2. You found the person who was yelling for help. It looks like they have been down here in this crater for some time.</p>

<p><strong>Do you help them? (Y/N)</strong></p>
'''
def friendwoot(choice=None):
    friend_Woot = friendwoot_statements() 
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_4_meet_woot.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''
    if not choice:
        return friend_Woot + background_script
    if choice == "y":
        return crater("")
    elif choice == "n":
        return goodbye("")
    else:
        return "Invalid choice. Try again."
def crater_statments():
    return '''
<p>Hi friend, thank you for coming down to help me.</p>
<p>I don't know how long I have been down here.</p>
<p>As you look around the crater, it is very dark, but you see there is a small door on the other side.</p>
<p><strong>What do you want to do next?</strong></p>
'''
def crater(choice=None):
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_5_the_door-1.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''
    crater_statment = crater_statments() 
    if not choice:
        return crater_statment +background_script
    if choice == "sit down with my friend":
        print("sit down with my friend")
        return note1("")
    if choice == "sit down next to my friend":
        return note1("")
    if choice == "talk with my friend please":
        return note1("")
    if choice == "talk to my friend please":
        return note1("")
    if choice == "talk to him":
        return note1("")
    if choice == "how can i help you":
        return note1("")
    if choice == "how do i help you":
        return note1("")
    if choice == "how can i help":
        return note1("")
    if choice == "how do i help":
        return note1("")
    if choice == "help":
        return note1("")
    if choice == "what is your name":
        return note1("")
    if choice == "ask more questions":
        return note1("")
    if choice == "ask questions":
        return note1("")
    if choice == "ask a question":
        return note1("")
    if choice == "question":
        return note1("")
    if choice == "where am i":
        return note1("")
    if choice == "why am i here":
        return note1("")
    elif choice == "enter door":
        return utunnel("")
    elif choice == "enter the door":
        return utunnel("")
    elif choice == "go in the door":
        return utunnel("")
    elif choice == "go into the door":
        return utunnel("")
    elif choice == "go through the door":
        return utunnel("")
    elif choice == "go to the door":
        return utunnel("")
    elif choice == "check out the door":
        return utunnel("")
    elif choice == "go inside the door":
        return utunnel("")
    elif choice == "go inside":
        return utunnel("")
    elif choice == "open the door":
        return utunnel("")
    elif choice == "open door":
        return utunnel("")
    else:
        print("Invalid choice. Try again.")
        crater()

def utunnel_statements():
    return '''
    You and your friend enter the small dark hallway
    Halfway through the hallway, your friend stops.
    'I am sorry friend, I cant leave. I extract my medicine from the crater down here.'
    Your friend hands you a note, but it is too dark to see and the hallway is too small to light a match. You see a light at the exit of the hallway. <br>
    What do you do next? 
'''
def utunnel(choice=None):
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_6_the_tunnel-1.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''
    utunnel_statement = utunnel_statements() 
    if not choice:
        return utunnel_statement + background_script
    if choice == "stay in":
        return '''You crawl back to the crater with your friend.''' + "<br>" + note2("")
        
    if choice == "return":
        return '''You crawl back to the crater with your friend.''' + "<br>" + note2("")
    if choice == "stay with my friend":
        return '''You crawl back to the crater with your friend.''' + "<br>" + note2("")
    if choice == "go back":
        return '''You crawl back to the crater with your friend.''' + "<br>" + note2("")
    if choice == "go back with my friend please":
        return '''You crawl back to the crater with your friend.''' + "<br>" + note2("")
    if choice == "return with my friend please":
        return '''You crawl back to the crater with your friend.''' + "<br>" + note2("")
    if choice == "talk with my friend":
        return '''You crawl back to the crater with your friend.''' + "<br>" + note2("")
    if choice == "talk to my friend":
        return '''You crawl back to the crater with your friend.''' + "<br>" + note2("")
    elif choice == "light a match stick":
        return '''The tunnel is too small to light a match.Try again.''' + "<br>" + utunnel("")
     
    elif choice == "read the note please":
        return '''The tunnel is too small to light a match.Try again.''' + "<br>" + utunnel("")
    
    elif choice == "exit":
        return ex1t("")
    elif choice == "exit the hallway":
        return ex1t("")
    elif choice == "exit hallway":
        return ex1t("")
    elif choice == "leave the hallway":
        return ex1t("")
    elif choice == "go to the exit":
        return ex1t("")
    elif choice == "leave hallway":
        return ex1t("")
    elif choice == "go to the light":
        return ex1t("")
    elif choice == "go to exit":
        return ex1t("")
    elif choice == "leave":
        return ex1t("")
    else:
        print("Invalid choice. Try again.")
        return utunnel("")
def note1_statements():
    return '''
    You sit down next to your friend and he hands you a note.
    You read the note from your friend and it says, 'Please dont leave.'
    What do you want to do next? (stay/leave me)
'''
def note1(choice=None):
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_8_the_note-1.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''
    note1_statment = note1_statements() 
    if not choice:
        return note1_statment +background_script

    if choice == "stay":
        return '''Thanks friend, I knew you were a good person. My name is Woot.
        I want to show you what I have built here.''' + "<br>" + treasure("")
    elif choice == "leave me":
        return goodbye("")

def note2_statements():
    return '''
You sit down next to your friend and you read the note and it says, 'Please dont leave.'
What do you want to do next? (stay/leave me) 
'''
def note2(choice=None):
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_8_the_note-1.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''
    note2_statment = note2_statements() 
    if not choice:
        return note2_statment + background_script

    if choice == "stay":
        return '''Thanks friend, I knew you were a good person. My name is Woot.
        I want to show you what I have built here.''' + "<br>" + treasure("")
    elif choice == "leave me":
        return goodbye("")

def treasure_statments():
    return '''
    Thanks friend, I knew you were a good person. My name is Woot.
    I want to show you what I have built here.
    Woot takes you to the dark side of crater
    'I have been building this plantation for years.
    'There is a stream down here which seems to give much energy to living things.
    'Look at all the trees full of fruit and rows of vegetables, isn't it wonderful?!
    'I want to share with you the treasure I've found here..
    Woot digs out a large box from under a tree trunk
    In excitement, you exclaim, 'Wow, loot!
    Thank you for playing! :)

'''
def treasure(choice = None):
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_9_treasure-1.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''
    treasure_statment = treasure_statments() 
    if not choice:
        return treasure_statment+background_script
    
def ending():
  print("Thank you for playing.")   
  exit()

def ex1t_statements():
    return '''
    You go to the exit of the hallway.
    You have exited the hallway and made it out of the crater.
    You see your spaceship close to the exit.
    What do you do next? '''

def ex1t(choice):
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_10_the_spaceship-1.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''
    ex1t_statment = ex1t_statements() 
    if not choice:
        return ex1t_statment + background_script
    if choice == "going back":
        return note2("")
    if choice == "return":
        return note2("")
    if choice == "return to the crater":
        return note2("")
    if choice == "return with my friend":
        return note2("")
    if choice == "go back with my friend":
        return note2("")
    if choice == "go back to the crater":
        return note2("")
    if choice == "go back in the crater":
        return note2("")
    if choice == "go back inside":
        return note2("")
    if choice == "look at the note":
        return '''For some reason you crawl back to the crater.''' + "<br>" + note2("")     
    if choice == "light a match":
        return '''For some reason you crawl back to the crater.''' + "<br>" + note2("")
    if choice == "read the note":
        return '''For some reason you crawl back to the crater.''' + "<br>" + note2("")
    if choice == "read note":
        return '''For some reason you crawl back to the crater.''' + "<br>" + note2("")
    elif choice == "go to the spaceship":
        return goodbye("")
    elif choice == "get on the spaceship":
        return goodbye("")
    elif choice == "go back to the spaceship":
        return goodbye("")
    elif choice == "return to the spaceship":
        return goodbye("")
    elif choice == "go to the ship":
        return goodbye("")
    elif choice == "get on the ship":
        return goodbye("")
    elif choice == "go back to the ship":
        return goodbye("")
    elif choice == "return to the ship":
        return goodbye("")
    else:
        print("Invalid choice. Try again")
        return ex1t("")


def goodbye(choice):
    background_script = '''
         <script>
            document.body.style.backgroundImage = "url('/static/img/TARAMADEM_11_goodbye-1.jpg')";  // Set background image
            document.body.style.backgroundSize = "cover";  // Optional: make the image cover the full screen
            document.body.style.backgroundPosition = "center center";  // Optional: center the background image
        </script>
    '''
    return '''You are now free to traverse space solitarily, bye friend..
            Thank you for playing.''' + background_script


@app.route("/",methods=["GET", "POST"])
def index():
    # Landing page with the "Enter World" button
    return render_template("index.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    stage = "start"
    game_statements = statements()
    result_data = game_data.get(stage, game_data["default"])
    result_image = result_data["image"]
    if request.method == "POST":
        # Get the user input from the form
        choice = request.form.get("choice", "").lower()
        if choice == "climb down" or choice == "use the rope" or choice == "help" or choice == "escape":
            stage = "default"
            return render_template("home.html", result=world(choice))
        elif choice in ["f", "g"]:
            stage = "explore"
            result_data = game_data.get(stage, game_data["default"])
            result_image = result_data["image"]

            return render_template("home.html", result=spiderroom(choice),image_path=f"/static/{result_image}")
        elif choice in ["y", "n"]:
            return render_template("home.html", result=friendwoot(choice))
        elif choice in [
            "sit down with my friend", "sit down next to my friend", "talk with my friend please",
            "talk to my friend please", "talk to him", "how can i help you", "how do i help you",
            "how can i help", "how do i help", "help", "what is your name", "ask more questions",
            "ask questions", "ask a question", "question", "where am i", "why am i here"
        ]:
            return render_template("home.html", result=crater(choice))

        elif choice in [
            "enter door", "enter the door", "go in the door", "go into the door",
            "go through the door", "go to the door", "check out the door", 
            "go inside the door", "go inside", "open the door", "open door"
        ]:
            return render_template("home.html", result=crater(choice))
    
        elif choice in [
                "stay in", "return", "stay with my friend", "go back", 
                "go back with my friend please", "return with my friend please", 
                "talk with my friend", "talk to my friend"
                ]:
            return render_template("home.html", result=utunnel(choice))
        elif choice in [
            "light a match stick", "read the note please"
        ]:
            return render_template("home.html", result=utunnel(choice))
        elif choice in [
            "exit", "exit the hallway", "exit hallway", "leave the hallway", 
            "go to the exit", "leave hallway", "go to the light", 
            "go to exit", "leave"
        ]:
            return render_template("home.html", result=utunnel(choice))
        elif choice == "stay":
            return render_template("home.html", result=note2(choice))
        elif choice == "leave me":
            return render_template("home.html", result=note1(choice))
        
        elif choice in [
            "going back", "return", "return to the crater", "return with my friend", 
            "go back with my friend", "go back to the crater", "go back in the crater", 
            "go back inside", "look at the note", "light a match", 
            "read the note", "read note"
        ]:

            return render_template("home.html", result=ex1t(choice))
        elif choice in [
                "go to the spaceship", "get on the spaceship", "go back to the spaceship", 
                "return to the spaceship", "go to the ship", "get on the ship", 
                "go back to the ship", "return to the ship"
            ]:      
            return render_template("home.html", result=ex1t(choice))
        else:
            return render_template("home.html", result="Invalid choice. Try again.",image_path=f"/static/{result_image}")

    return render_template("home.html", result=game_statements ,image_path=f"/static/{result_image}")

if __name__ == "__main__":
    app.run(debug=True)
