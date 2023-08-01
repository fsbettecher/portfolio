import pandas as pd
url = 'https://dados.mobilidade.rio/gps/brt'

brt_gps = pd.read_json(url)

brt_gps = brt_gps['veiculos'].tolist()

brt_gps = pd.DataFrame.from_dict(brt_gps)

teste = brt_gps.to_csv()