########## IMPORT ##########
from flask import Flask, render_template
import config
########## endimport ##########

########## FLASK SETUP ##########
app = Flask(__name__)
app.config.from_object(config)
########## endflasksetup ##########

########## INDEX VIEW ##########
@app.route('/')
def show_count():
	return render_template('index.html')
########## endindexview ##########


########## RUN APP ##########
if __name__ == "__main__":
    app.run(debug = True)
########## endrunapp ##########