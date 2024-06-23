from flask import Flask, request, render_template, session, redirect, url_for
from gues import TahminOyunu

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Flask oturumları için gerekli

@app.route('/imax')
def index():
    if 'oyun' not in session:
        session['oyun'] = TahminOyunu().__dict__
    return render_template('index.html')

@app.route('/tahmin', methods=['POST'])
def tahmin():
    tahmin = request.form.get('tahmin')
    oyun = TahminOyunu()
    oyun.__dict__.update(session['oyun'])
    mesaj, devam = oyun.tahmin_et(tahmin)
    session['oyun'] = oyun.__dict__
    return render_template('deneme.html.html', mesaj=mesaj, devam=devam)

@app.route('/reset')
def reset():
    session.pop('oyun', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
