from app import app
from flask import render_template
import requests
from lxml import html


@app.route('/')
@app.route("/index")
def index():

    return render_template('index.html')

@app.route('/algodao')
def algodao():
    pagina = requests.get("https://wikifarmer.com/pt-br/informacoes-da-planta-de-algodao/")
    dados = html.fromstring(pagina.content)
    sobreAlgodao = dados.xpath('/html/body/div/div[1]/article/main/div/div/div[1]/div[1]/p[2]/text()')

    return render_template('algodao.html', algodao=sobreAlgodao)

@app.route('/cafe')
def cafe():
    pagina = requests.get("https://www.gov.br/agricultura/pt-br/assuntos/politica-agricola/cafe/cafeicultura-brasileira")
    dados = html.fromstring(pagina.content)
    sobreCafe = dados.xpath('/html/body/div[3]/div[1]/main/div[2]/div/div[4]/div/p[1]/text()')

    return render_template('cafe.html', cafe=sobreCafe)

@app.route('/cana')
def cana():
    pagina = requests.get("https://www.infoescola.com/plantas/cana-de-acucar/")
    dados = html.fromstring(pagina.content)
    sobreCana = dados.xpath('/html/body/div[2]/div[1]/div[2]/article/p[1]/text()')

    return render_template('cana.html', cana=sobreCana)

@app.route('/milho')
def milho():
    pagina = requests.get("https://www.infoescola.com/plantas/milho/")
    dados = html.fromstring(pagina.content)
    sobreMilho = dados.xpath('/html/body/div[2]/div[1]/div[2]/article/p[3]/text()')
    return render_template('milho.html', milho=sobreMilho)

@app.route('/soja')
def soja():
    pagina = requests.get("https://aprosojabrasil.com.br/a-soja/")
    dados = html.fromstring(pagina.content)
    sobreSoja = dados.xpath('/html/body/div[2]/div[4]/div/div[1]/div/div/div/div[3]/div/p[27]/text()')
    return render_template('soja.html', soja=sobreSoja)

@app.route('/trigo')
def trigo():
    pagina = requests.get("https://www.infoescola.com/plantas/trigo/")
    dados = html.fromstring(pagina.content)
    sobreTrigo = dados.xpath('/html/body/div[2]/div[1]/div[2]/article/p[2]/text()')
    return render_template('trigo.html', trigo=sobreTrigo)





