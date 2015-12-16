import sys
import random

import numpy as np 
import xgboost as xgb 

from utils import read_data, write_answer, split_data

train_fname = sys.argv[1]
test_fname = sys.argv[2]
output_fname = sys.argv[3]


def main():
    train_x, train_y = read_data(train_fname)
    ID, test_x = read_data(test_fname, train_mode=False)
    print(ID)
    print(train_x)
    print(np.sum(train_y))

    ind = random.shuffle(range(train_x[0]))
    # train_x, train_y, val_x, val_y = split_data(train_x, train_y, val_ratio=0.2)

    tr = xgb.DMatrix(train_x, label=train_y)
    # val = xgb.DMatrix(val_x, label=val_y)
    te = xgb.DMatrix(test_x)

    param = {'bst:max_depth':3, 'bst:eta':0.1, 'silent':0, 'objective':'binary:logistic' }
    param['nthread'] = 16
    param['eval_metric'] = 'auc'

    num_round = 100

    xgb.cv(param, tr, num_round, nfold=5, metrics={"error"})

    model = xgb.train(param, tr, num_round, early_stopping_rounds=10)

    ypred = model.predict(xgmat, ntree_limit=model.best_ntree_limit)

    clf = RandomForestClassifier(n_estimators=500,
                                 criterion='entropy',
                                 max_features='sqrt',
                                 max_depth=None,
                                 oob_score=False,
                                 n_jobs=-1,
                                 verbose=1)

    clf.fit(X=train_x, y=train_y)
    print(clf.score(train_x, train_y))
    pred = clf.predict(X=test_x)
    pred_prob = clf.predict_proba(X=test_x)[:,1]

    write_answer(output_fname, ID, pred, print_prob=False)
    write_answer("prob_"+output_fname, ID, pred_prob, print_prob=True)


if __name__ == "__main__":
    main()