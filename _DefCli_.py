import requests

def previsao_do_tempo(data):
    resposta = requests.get("https://ipapi.co/json/")

    if resposta.status_code != 200:
        print("Erro! Não foi possível obter a localização.")

    dados = resposta.json()
    if "latitude" in dados and "longitude" in dados:
        latitude = dados["latitude"]
        longitude = dados["longitude"]
    else:
        print("Erro! Não foi possível obter a localização.")
        print(dados)
        return

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        "&timezone=auto"
    )

    resposta1 = requests.get(url)

    if resposta1.status_code == 200:
        dados = resposta1.json()
        data_procurada = data

        datas = dados["daily"]["time"]
        maximas = dados["daily"]["temperature_2m_max"]
        minimas = dados["daily"]["temperature_2m_min"]
        chuvas = dados["daily"]["precipitation_sum"]

        if data_procurada in datas:
            indice = datas.index(data_procurada)
            print("Data:", data_procurada)
            print("Máxima:", maximas[indice], "°C")
            print("Mínima:", minimas[indice], "°C")
            print(f"Chuva prevista para {data_desejada}: {chuvas[indice]} mm")

    if chuvas[0] > 10:
        print("Atenção: há previsão de chuva significativa para essa data.")
    else:
        print("Condições favoráveis para o transporte.")