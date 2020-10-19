from flask import Flask, request
from datetime import datetime
from final1 import *

app = Flask(__name__)


print("Hello World")

#print(do_something())

#lx= main_fun()

#pprint(lx)

print("Hello World1")

@app.route('/')
def hello_world():
 
    if 'num' in request.args:
        num = request.args['num']
    if 'num2' in request.args:
    	num2 = request.args['num2']
    else:
        num = '0' 
        num2 ='0'

    # num = request.args.get('num', 1)
    print(request.args, num)
    heading = '<h1>' + num + '</h1>' 
    return heading +  '''

        <form action="">
            <select name="num">
                <option value="1">One</option>
                <option value="2">Two</option>
            </select>
            
        
            <select name="num2">
                <option value="25">Region One</option>
                <option value="26">Region Two</option>
            </select>
            <input type="submit" />
        </form>

        <table style="width:100%">''' + main_fun(num,num2,"today") + ' </table> '

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

#http://127.0.0.1:5000/



# this is a testing line to check waether its going to add to the github