import pandas as pd

url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv'
dados = pd.read_csv(url)
print('forma dos dados')
print(dados.shape)
print('Dados iniciais')
print(dados.head)
print('Dados iniciais - 20 linhas')
print(dados.head(20))
