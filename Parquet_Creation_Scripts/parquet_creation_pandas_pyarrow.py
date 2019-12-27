# %%
import pyarrow as pa
import pyarrow.parquet as pq
import pathlib
import pandas as pd

p = pathlib.Path(__file__).parent.parent
print(p)

Original_Data = p / "Original_Data"
Parquet_Files = p / "Parquet_Files"

compression_types = ["NONE", "SNAPPY", "GZIP", "ZSTD"]

for compression_type in compression_types:
    csv_files = Original_Data.glob("*.csv")
    for file in csv_files:
        filename = (
            str(Parquet_Files.resolve())
            + "\\"
            + compression_type
            + "_pandas_pyarrow_"
            + file.stem
            + ".parquet"
        )
        dta = pd.read_csv(file, delimiter="|")
        schema = pa.Schema.from_pandas(dta)
        dta = pa.Table.from_pandas(dta)
        pq.ParquetWriter(filename, schema=schema, compression=compression_type)
