import tensorflow as tf
import pandas as pd
import numpy as np
import shutil

print(tf.__version__)
tf.logging.set_verbosity(tf.logging.INFO)

# In CSV, label is the first column, after the features, followed by the key
CSV_COLUMNS = ['fare_amount', 'pickuplon', 'pickuplat', 'dropofflon', 'dropofflat', 'passengers', 'key']
FEATURES = CSV_COLUMNS[1:len(CSV_COLUMNS) - 1]
LABEL = CSV_COLUMNS[0]
DEFAULTS = [[0.0], [-74.0], [40.0], [-74.0], [40.7], [1.0], ['nokey']]


# Create an input function that stores your data into a dataset
def read_dataset(filename, mode, batch_size=512):
    def _input_fn():
        def decode_csv(value_column):
            columns = tf.decode_csv(value_column, record_defaults=DEFAULTS)
            features = dict(zip(CSV_COLUMNS, columns))
            label = features.pop(LABEL_COLUMN)
            return features, label

        # Create list of files that match pattern
        file_list = tf.gfile.Glob(filename)

        # Create dataset from file list
        dataset = tf.data.TextLineDataset(file_list).map(decode_csv)

        if mode == tf.estimator.ModeKeys.TRAIN:
            num_epochs = None  # indefinitely
            dataset = dataset.shuffle(buffer_size=10 * batch_size)
        else:
            num_epochs = 1  # end-of-input after this

        dataset = dataset.repeat(num_epochs).batch(batch_size)
        return dataset.make_one_shot_iterator().get_next()

    return _input_fn


# Define your feature columns
def make_feature_cols():
    INPUT_COLUMNS = [
        tf.feature_column.numeric_column('pickuplon'),
        tf.feature_column.numeric_column('pickuplat'),
        tf.feature_column.numeric_column('dropofflat'),
        tf.feature_column.numeric_column('dropofflon'),
        tf.feature_column.numeric_column('passengers'),
    ]

    def add_more_features(feats):
        # Nothing to add (yet!)
        return feats

    all_feature_cols = add_more_features(INPUT_COLUMNS)

    return all_feature_cols


shutil.rmtree(OUTDIR, ignore_errors=True)  # start fresh each time

model = tf.estimator.LinearRegressor(
    feature_columns=feature_cols,
    model_dir=OUTDIR
)

model.train(
    input_fn=read_dataset('./taxi-train.csv', mode=tf.estimator.ModeKeys.TRAIN),num_epochs=100)
)

def print_rmse(model, name, df):
    metrics = model.evaluate(
        input_fn=read_dataset('./taxi-valid.csv', mode=tf.estimator.ModeKeys.EVAL)
    )
    print('RMSE on {} dataset = {}'.format(name, np.sqrt(metrics['average_loss'])))


print_rmse(model, 'validation', df_valid)
