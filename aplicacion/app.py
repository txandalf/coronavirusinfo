from flask import Flask, render_template, request, redirect
from aplicacion import covid_data


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/', methods=["POST", "GET"])
def inicio(cty="Spain"):
    country = cty
    if request.method=="POST":
        country = request.form.get("country")
        print(country)

    try:
        data = covid_data.getCountryInfo(country)
        countries = covid_data.getCountryList()
        #data = "helo world"
        return render_template("inicio.html", data=data, country=country, countries=countries)
    except:
        return render_template("inicio.html", data=covid_data.getCountryInfo("spain"), country="spain",
            countries=covid_data.getCountryList())
