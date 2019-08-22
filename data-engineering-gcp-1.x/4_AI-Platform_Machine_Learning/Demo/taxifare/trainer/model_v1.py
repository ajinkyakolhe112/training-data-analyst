import tensorflow as tf
import pandas as pd
import numpy as np
import shutil

print(tf.__version__)
tf.logging.set_verbosity(tf.logging.INFO)

# In CSV, label is the first column, after the features, followed by the key
CSV_COLUMNS = ['fare_amount', 'pickuplon', 'pickuplat', 'dropofflon', 'dropofflat', 'passengers', 'key']
FEATURES = CSV_COLUMNS[1 : len(CSV_COLUMNS) - 1]
LABEL = CSV_COLUMNS[0]


# Create an input function that stores your data
def make_input_fn(df, num_epochs, shuffle=True):
    return tf.estimator.inputs.pandas_input_fn(
        x=df,
        y=df[LABEL],
        batch_size=128,
        num_epochs=num_epochs,
        shuffle=shuffle,
        queue_capacity=1000,
        num_threads=1,
    )


def make_feature_cols():
    input_columns = [tf.feature_column.numeric_column(k) for k in FEATURES]
    return input_columns


OUTDIR = "taxi_trained"
shutil.rmtree(path=OUTDIR, ignore_errors=True)  # start fresh each time

model = tf.estimator.LinearRegressor(
    feature_columns=make_feature_cols(), model_dir=OUTDIR
)

model.train(
    input_fn=make_input_fn(
        df=pd.read_csv(filename="../../taxi-train.csv", header=None, names=CSV_COLUMNS),
        num_epochs=1,
    )
)


def print_rmse(model, name):
    metrics = model.evaluate(
        input_fn=make_input_fn(
            df=pd.read_csv(
                filename="../../taxi-valid.csv", header=None, names=CSV_COLUMNS
            ),
            num_epochs=1,
        )
    )
    print("RMSE on {} dataset = {}".format(name, np.sqrt(metrics["average_loss"])))


print_rmse(model, "validation")
