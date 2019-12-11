import json
def read_txt(filename):
    with open("./data/"+filename,"r",encoding="utf-8") as f:
        result = []
        for data in f.readlines():
            result.append(list(data.strip().split(",")))

        return result[1::]



if __name__ == '__main__':
    print(read_txt("employee_post.txt"))