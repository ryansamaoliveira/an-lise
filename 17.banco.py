import polars as pl
from sqlalchemy import create_engine

PARQUET_PATH = r'C:/Users/martins.ryan/an-lise/dados_bronze/df_base.parquet'
TABELA = 'bolsa_familia'
BATCH_SIZE = 10000
ENGINE_URL = ('mysql+pymysql://root:@localhost:3306/bolsa_familia')

engine = create_engine(ENGINE_URL)

print('Lendo o arquivo Parquet')
df = pl.read_parquet(PARQUET_PATH)

total = df.shape[0]
linhas = 0

for i, batch in enumerate(df.iter_slices(n_rows=BATCH_SIZE)):
    batch_pd = batch.to_pandas()

    modo = 'replace' if i == 0 else 'append'

    batch_pd.to_sql(name=TABELA, con=engine, if_exists=modo, index=False)
    linhas += batch_pd.shape[0]
    percent = (linhas / total) * 100
    print(f'Lote {i + 1}: {percent}%')

print('Escrita Finalizada')