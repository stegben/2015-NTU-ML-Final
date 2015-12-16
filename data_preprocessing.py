import sys
import pandas as pd

input_fname = sys.argv[1]
output_fname = sys.argv[2]

data = pd.read_csv(input_fname)

data["uln/cln"] = data.user_log_num / data.course_log_num
data["uln/tcn"] = data.user_log_num / data.take_course_num
data["cln/tun"] = data.course_log_num / data.take_user_num
data["ln/uln"] = data.log_num / data.user_log_num
data["ln/uln/tcn"] = data["ln/uln"] / data.take_course_num
data["lc/cln"] = data.log_num / data.course_log_num
data["lc/cln/tun"] = data["lc/cln"] / data.take_user_num

if "ans" in data.columns:
    ans = data["ans"]
    data.drop(labels=["ans"], axis=1, inplace=True)
    data.insert(len(data.columns), 'ans', ans)

print(data)

data.to_csv(output_fname, index=False)