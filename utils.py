import numpy as np

def read_data(fname, train_mode=True):
    x = []
    y = []
    ID = []
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
                ID.append(data[0])
    x = np.array(x)
    y = np.array(y) 
    if train_mode: 
        return x, y
    else:
        return ID, x



def write_answer(fname, ID, pred, print_prob):
    pred = list(pred)
    if print_prob:
        pred = [str(p) for p in pred]
    else:
        pred = [str(int(p)) for p in pred]
    
    ID = list(ID)
    ID = [str(int(i)) for i in ID]

    with open(fname, "w") as f:
        for i, p in zip(ID, pred):
            f.write(i + "," + p + "\n")