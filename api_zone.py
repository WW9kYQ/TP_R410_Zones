import requests, urllib.parse
from flask import Flask, jsonify, request, json
app = Flask(__name__)

zone = [
    {
        "nom": "Zone B"
    }
]



@app.route('/')
def accueil():
    return "Bonjour"


@app.route('/zones', methods=['GET'])
def getZones():
    url = "https://data.education.gouv.fr/api/records/1.0/search/?dataset=fr-en-calendrier-scolaire&q=%22Zone+A%22+or+%22Zone+B%22+or+%22Zone+C%22&rows=1000"
    r = requests.request('GET',url)
    data = r.json()
    tab_zone=[]

    for item in data["records"]:
        dico = {"zone":item["fields"]["zones"]}
        if dico not in tab_zone:
            tab_zone.append(dico)
        else:
            continue
    return tab_zone


@app.route('/zones/villes', methods=['GET'])
def getZonesByVille():
    ville = urllib.parse.quote(request.args.to_dict()['ville'])
    url = "https://data.education.gouv.fr/api/records/1.0/search/?dataset=fr-en-annuaire-education&q={}&rows=1&exclude.type_etablissement=Ecole".format(ville)
    r = requests.request('GET', url)
    data = r.json()
    tab_zone = []

    

    # TODO
    return jsonify(zone)


@app.route('/zones/adresses', methods=['POST'])
def getZonesByAdresse():
    # TODO
    return jsonify(zone)



if __name__ == '__main__':
    time.sleep(30)
    app.run(host='0.0.0.0', port=5050)