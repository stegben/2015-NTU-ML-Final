import sys

import numpy as np 
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold

train_fname = sys.argv[1]
test_fname = sys.argv[2]
output_fname = sys.argv[3]


def read_data(fname, train_mode=True):
    x = []
    y = []
    with open(fname, "r") as f:
        f.readline()
        for line in f:
            data = line.rstrip().split(",")
            data = [float(d) for d in data]
            if train_mode:
                x.append(data[1:-1])
                y.append(data[-1])
            else:
                x.append(data[1:])
    x = np.array(x)
    y = np.array(y) if train_mode else None
    return x, y


def main():
    train_x, train_y = read_data()
    print(X.values.shape)
    print(Y.values.shape)

    # clf = RandomForestClassifier(n_estimator=1000)


if __name__ == "__main__":
    main()
