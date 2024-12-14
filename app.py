from flask import Flask, render_template #render_template helps to render html files
from random import randint  # Import randint from random module

# Create an instance of the Flask class. This is the web application.
app = Flask(__name__) # app is the name it can be anything

# This is the route for the home page.
@app.route("/")
def index():
    return "Flask App!"  # This simply returns the text "Flask App!" when you visit the homepage.

# This is a dynamic route. The part <string:name> is a placeholder for a name in the URL.
@app.route("/hello/<string:name>/")
def hello(name):
    # This renders an HTML template and passes a variable (name) to it.
    # return render_template("test.html", name=name)
    # List of quotes
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann",
        "'Computer science is no more about computers than astronomy is about telescopes' -- Edsger Dijkstra",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"
    ]
    
    # Choose a random quote from the list
    random_number = randint(0, len(quotes) - 1)
    quote = quotes[random_number]
    
    # Render the template and pass the name and quote to it
    return render_template('test.html', name=name, quote=quote) 

# Start the Flask web server. It's set to listen on all IP addresses (0.0.0.0) on port 80.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
