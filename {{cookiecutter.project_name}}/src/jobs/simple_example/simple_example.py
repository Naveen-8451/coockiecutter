# simple_example.py
from pyspark.sql.types import StructType, StructField, StringType
import shutil


def main(initializer, cycle_date, source_directory, source_file, target_directory, target_file):
    # Job entry point
    spark = initializer.spark
    logger = initializer.LOGGER
    config = initializer.config
    file_wrapper = initializer.io

    try:

        # This is a simple example job used to show the basics of how our jobs should be structured, how to pass in
        # parameters, how to use the config file, and how to do basic read/writes.

        print('This is an simple_example job!')
        print('The source file location is: ' + source_directory)
        print('The source file name is: ' + source_file)
        print('The target file location is: ' + target_directory)
        print('The target file name is: ' + target_file)
        print('The cycle date is: ' + cycle_date)
        print('Example config data: ' + config['example']['simple_example'])

        schema = StructType([
            StructField('symbol', StringType(), True),
            StructField('sector', StringType(), True),
            StructField('price', StringType(), True),
            StructField('price_to_earnings', StringType(), True),
            StructField('dividend', StringType(), True),
            StructField('yield', StringType(), True),
            StructField('earnings_to_share', StringType(), True),
            StructField('52_week_low', StringType(), True),
            StructField('52_week_high', StringType(), True),
            StructField('market_cap', StringType(), True),
            StructField('ebitda', StringType(), True),
            StructField('price_to_sales', StringType(), True),
            StructField('price_to_book', StringType(), True),
            StructField('sec_filings', StringType(), True)])

        my_data = spark.read.csv(source_directory + source_file, header='true', schema=schema)

        my_data.show()

        my_data.printSchema()

        my_data.write.mode('overwrite').parquet(target_directory + target_file + cycle_date)

    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))
    finally:
        spark.stop()