from config import app
import routes

@app.route('/')
def greet():
    return "Hello Flask app is running and it has to run continously despite changes!!!"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")