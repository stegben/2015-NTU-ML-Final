import sys

import numpy as np 
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold

from utils import read_data, write_answer

train_fname = sys.argv[1]
test_fname = sys.argv[2]
output_fname = sys.argv[3]


def main():
    train_x, train_y = read_data(train_fname)
    ID, test_x = read_data(test_fname, train_mode=False)
    print(ID)
    print(train_x)
    print(np.sum(train_y))

    clf = RandomForestClassifier(n_estimators=10000,
                                 criterion='gini',
                                 max_features=auto,
                                 max_depth=None,
                                 oob_score=True,
                                 n_jobs=-1,
                                 verbose=1)

    clf.fit(X=train_x, y=train_y)
    print(clf.oob_score_)
    print(clf.score(train_x, train_y))
    pred = clf.predict(X=test_x)
    pred_prob = clf.predict_proba(X=test_x)[:,1]

    write_answer(output_fname, ID, pred, print_prob=False)
    write_answer("prob_"+output_fname, ID, pred_prob, print_prob=True)


if __name__ == "__main__":
    main()
