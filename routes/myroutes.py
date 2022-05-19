from config import app

@app.get('/home')
def greetnow():
    return "This is home page...Hope you are doing good!!!!"

@app.get('/sample')
def fun():
    return " This is a sample page"