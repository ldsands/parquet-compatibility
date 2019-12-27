# parquet-compatibility

Compatibility tests to make sure Julia can read parquet files from pyarrow output (open to adding others pyarrow is what I am familiar with so that is what I used)

## Original_Data

Contains the original csv files used as the basis for the parquet files

## Parquet_Creation_Scripts

This holds the scripts for the creation of the parquet files (right now only using pandas and pyarrow in python I'm open to other options as well)

## Parquet_Files

Stores all the parquet files to be tested (I'm open to adding more types of data to this for additional testing)
