from datetime import datetime as dt

from flask import Flask, redirect

from updater import update_resume, dl_count

app = Flask(__name__, static_folder='')

update_date = 0

# config info
template_values = {'dlt': dl_count(['swaglyrics', 'SwSpotify'])}


@app.route('/')
def hello():
    return redirect('https://aadibajpai.me')


@app.route('/aadi_resume.pdf')
def resume():
    global update_date
    print(f"resume last updated at {update_date}")
    date_now = dt.today()
    # pepy updates at 5pm UTC https://github.com/psincraian/pepy#faq
    if date_now.day > update_date and date_now.hour > 16 or update_date == 0:
        update_resume(template_values)
        update_date = date_now.day
        print(f"resume updated now at {update_date}")
    return app.send_static_file('aadi_resume.pdf')


if __name__ == '__main__':
    app.run()
