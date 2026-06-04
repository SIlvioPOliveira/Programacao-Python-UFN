import requests


class CidadeClima:
    def __init__(self, nome, temperatura, umidade, condicao):
        # Atributos encapsulados/privados
        self.__nome = nome
        self.__temperatura = temperatura
        self.__umidade = umidade
        self.__condicao = condicao


    def __str__(self):
        return f" {self.__nome:<12} |  {self.__temperatura:>5.1f}°C |  Umidade: {self.__umidade:>3}% |  {self.__condicao.capitalize()}"


def main():
    API_KEY = "11f15d8b8901975e692ed92fbc778eed" 
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    
    cidades_pesquisa = ['São Paulo', 'London', 'Tokyo', 'New York', 'Paris', 'CidadexInvalida']
    
    
    relatorio_clima = []

    print("Buscando dados climáticos aguarde...\n")

    for cidade in cidades_pesquisa:
        try:
            
            params = {
                "q": cidade,
                "appid": API_KEY,
                "units": "metric",
                "lang": "pt_br"
            }
            
            response = requests.get(BASE_URL, params=params)

            
            if response.status_code == 200:
                dados_json = response.json()

                nome = dados_json["name"]
                temperatura = dados_json["main"]["temp"]
                umidade = dados_json["main"]["humidity"]
                condicao = dados_json["weather"][0]["description"]

                
                obj_clima = CidadeClima(nome, temperatura, umidade, condicao)
                
               
                relatorio_clima.append(obj_clima)

            elif response.status_code == 404:
                print(f" Erro: A cidade '{cidade}' não foi encontrada. Verifique a digitação.")
            elif response.status_code == 401:
                print(" Erro 401: API Key inválida. Verifique sua chave do OpenWeatherMap.")
                break # Para o loop se a chave estiver errada
            else:
                print(f" Erro desconhecido na cidade '{cidade}'. Código: {response.status_code}")

        except requests.exceptions.RequestException as e:
             print(f" Erro de conexão de rede ao buscar '{cidade}': {e}")

   
    print("\n" + "="*60)
    print(" RELATÓRIO CLIMÁTICO ATUAL")
    print("="*60)
    
    
    if relatorio_clima:
        for clima in relatorio_clima:
            print(clima)
    else:
        print("Nenhum dado climático pôde ser recuperado.")
    
    print("="*60)

if __name__ == "__main__":
    main()