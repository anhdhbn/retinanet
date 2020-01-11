path = "/home/anhdh/projects/keras-retinanet/dataset/data"

with open("./train.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

content = [ "{}/{}".format(path, data) for data in content]

with open('./train_edited.txt', 'w') as f:
    for item in content:
        data = item.split(",")
        last = data[-1]
        data = data[:-1]

        result = ",".join(data)
        if last ==  "0":
            result = result + ",loai_1"
        elif last == "1":
            result = result + ",loai_2"
        f.write("%s\n" % result)



with open("./val.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

content = [ "{}/{}".format(path, data) for data in content]

with open('./val_edited.txt', 'w') as f:
    for item in content:
        data = item.split(",")
        last = data[-1]
        data = data[:-1]

        result = ",".join(data)
        if last ==  "0":
            result = result + "loai_1"
        elif last == "1":
            result = result + "loai_2"
        f.write("%s\n" % result)