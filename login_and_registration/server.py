from app import app
from app.controllers import users #<--controllers

if __name__=="__main__":
	app.run(debug=True)