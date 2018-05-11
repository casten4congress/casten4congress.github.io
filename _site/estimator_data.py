import pandas as pd
import tensorflow as tf

TRAIN_URL = "election_data_training_dem.csv"
TEST_URL = "election_data_testing.csv"

CSV_COLUMN_NAMES = ['precinct','election_year','num_dem_primary','num_rep_primary','num_dem_cand_primary','num_dem_primary_challengers','num_rep_primary_challengers','dem_cand_gender','per_pop_white','per_pop_hispanic','per_pop_20-24','per_pop_25-34','per_pop_35-44','per_pop_45-54','per_pop_55-59','per_pop_60-64','per_pop_65-74','per_pop_75-84','per_pop_85','per_pop_10-15K','per_pop_15-25K','per_pop_25-35K','per_pop_35-50K','per_pop_50-75K','per_pop_75-100K','per_pop_100-150K','per_pop_150-200K','per_pop_200K','per_pop_9-12','per_pop_AD','per_pop_BD','per_pop_GD','per_pop_HSG','per_pop_less9','per_pop_some_college','num_dem_gen']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']

def maybe_download():
    train_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)
    test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)

    return train_path, test_path

def load_data(y_name='num_dem_gen'):
    """Returns the iris dataset as (train_x, train_y), (test_x, test_y)."""
    # train_path, test_path = maybe_download()

    train = pd.read_csv(TRAIN_URL, names=CSV_COLUMN_NAMES, header=1)
    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(TEST_URL, names=CSV_COLUMN_NAMES, header=0)
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset


def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset


# The remainder of this file contains a simple example of a csv parser,
#     implemented using a the `Dataset` class.

# `tf.parse_csv` sets the types of the outputs to match the examples given in
#     the `record_defaults` argument.
CSV_TYPES = [[0.0], [0.0], [0.0], [0.0], [0]]

def _parse_line(line):
    # Decode the line into its fields
    fields = tf.decode_csv(line, record_defaults=CSV_TYPES)

    # Pack the result into a dictionary
    features = dict(zip(CSV_COLUMN_NAMES, fields))

    # Separate the label from the features
    label = features.pop('num_dem_gen')

    return features, label


def csv_input_fn(csv_path, batch_size):
    # Create a dataset containing the text lines.
    dataset = tf.data.TextLineDataset(csv_path).skip(1)

    # Parse each line.
    dataset = dataset.map(_parse_line)

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset
