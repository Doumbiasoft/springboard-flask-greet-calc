# Put your app in here.
from flask import Flask,request
import operations

app = Flask(__name__)

@app.route("/")
def index():
    html= f"""
    <html>
        <head>
        <title>Welcome!</title>
        </head>
        <body>
        <h1>Welcome to flask calc !</h1>
        </body>
    </html>
    """
    return  html

@app.route("/<string:operation>")
def calculator(operation):
 
     a = float(request.args.get("a", 0))
     b = float(request.args.get("b", 0))
     match operation:
           case "add":
                 return showHtml(operations.add(a,b))
           case "sub":
                 return showHtml(operations.sub(a,b))
           case "mult":
               return showHtml(operations.mult(a,b))
           case "div":
               return showHtml(operations.div(a,b))

@app.route("/math/<string:operation>")
def calculator_math(operation):
    
     if request.args.get("a") is None or request.args.get("b") is None:
          return showHtml("Parameters 'a' and/or 'b' are missing !")
     if request.args.get("a")=="" or request.args.get("b")=="":
          return showHtml(0)
     
     a = float(request.args.get("a", 0))
     b = float(request.args.get("b", 0))
     match operation:
           case "add":
                 return showHtml(operations.add(a,b))
           case "sub":
                 return showHtml(operations.sub(a,b))
           case "mult":
               return showHtml(operations.mult(a,b))
           case "div":
               return showHtml(operations.div(a,b))
        


def showHtml(text):
      """generate html for a given text"""
      
      html= f"""
        <html>
            <head>
            <title>Calc</title>
            </head>
            <body>
            <h1>{text}</h1>
            </body>
        </html>
        """
      return  html
