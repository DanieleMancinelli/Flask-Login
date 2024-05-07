from flask import Flask, request, redirect, url_for, render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template("login.html")

# Route per la verifica del login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    df = pd.read_csv('/workspace/Flask-Login/data/dati_utenti.csv')

    user = df[(df["Username"] == username) & (df["Password"] == password)]

    if not user.empty:
        # Estrai il nome e il cognome, assicurandoti di non mostrare l'username
        nome = user.iloc[0]["Nome"]
        
        return redirect(url_for('dashboard', nome=nome))
    else:
        return "Invalid username or password", 401

# Route per mostrare solo il nome dopo il login
@app.route('/dashboard/<nome>')
def dashboard(nome):
    return f"Benvenuto/a {nome}"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)