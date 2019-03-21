from flask import Flask, url_for
from updater import update_resume

app = Flask(__name__, static_folder='')

@app.route('/aadi_resume')
def resume():
  update_resume()
  return app.send_static_file('aadi_resume.pdf')

if __name__ == '__main__':
	app.run()