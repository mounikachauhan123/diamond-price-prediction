from flask import Flask,jsonify,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
if __name__=='main':
    app.run