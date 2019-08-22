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
DEFAULTS = [[0.0], [-74.0], [40.0], [-74.0], [40.7], [1.0], ["nokey"]]


# Create an input function that stores your data into a dataset
def read_dataset(filename, mode, batch_size=512):
    def _input_fn():
        def decode_csv(value_column):
            columns = tf.decode_csv(value_column, record_defaults=DEFAULTS)
            features = dict(zip(CSV_COLUMNS, columns))
            label = features.pop(LABEL)
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
    input_columns = [tf.feature_column.numeric_column(k) for k in FEATURES]

    def add_more_features(feats):
        # Nothing to add (yet!)
        return feats

    all_feature_cols = add_more_features(input_columns)

    return all_feature_cols


# Create your serving input function so that your trained model will be able to serve predictions
def serving_input_fn():
    feature_placeholders = {
        "pickuplon": tf.placeholder(tf.float32, [None]),
        "pickuplat": tf.placeholder(tf.float32, [None]),
        "dropofflat": tf.placeholder(tf.float32, [None]),
        "dropofflon": tf.placeholder(tf.float32, [None]),
        "passengers": tf.placeholder(tf.float32, [None]),
    }
    features = {
        key: tf.expand_dims(tensor, -1) for key, tensor in feature_placeholders.items()
    }
    return tf.estimator.export.ServingInputReceiver(features, feature_placeholders)


# Create an estimator that we are going to train and evaluate
def train_and_evaluate(output_dir, num_train_steps):
    estimator = tf.estimator.LinearRegressor(
        model_dir=output_dir, feature_columns=make_feature_cols()
    )

    train_spec = tf.estimator.TrainSpec(
        input_fn=read_dataset(
            filename="../../taxi-train.csv", mode=tf.estimator.ModeKeys.TRAIN
        ),
        max_steps=num_train_steps,
    )

    exporter = tf.estimator.LatestExporter(
        name="exporter", serving_input_receiver_fn=serving_input_fn
    )

    eval_spec = tf.estimator.EvalSpec(
        input_fn=read_dataset(
            filename="../../taxi-valid.csv", mode=tf.estimator.ModeKeys.EVAL
        ),
        steps=None,
        start_delay_secs=1,  # start evaluating after N seconds
        throttle_secs=10,  # evaluate every N seconds
        exporters=exporter,
    )

    tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)


OUTDIR = "taxi_trained"
shutil.rmtree(path=OUTDIR, ignore_errors=True)  # start fresh each time

train_and_evaluate(OUTDIR, num_train_steps=5000)
