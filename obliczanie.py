from flask import Flask, url_for, redirect, request, make_response, render_template

app = Flask(__name__)

# Szablon glowna.html wyświetla formularz umożliwiający wpisnie napiecia i natezenia, oraz wysłanie go do strony /wynik
@app.route("/glowna")
def wyswietl_glowna():
    return render_template("glowna.html")


# Strona /wynik odczytuje dane przesłane z formularza i wyświetla je przy pomocy szablonu wynik.html.
@app.route('/wynik', methods = ['POST','GET'])
def obsluga_formularza():

    if request.method == 'POST':
        u = float(request.form['u'])
        i = float(request.form['i'])
        r = str(u/i)
        return render_template('wynik.html', wynik = u/i)
    else:
        return redirect(url_for('wyswietl_glowna'))


if __name__ == "__main__":
    app.run(debug=True)
