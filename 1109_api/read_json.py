import json


def read_from_json(json_url):
    with open(json_url,'r') as json_file:
        j = json.load(json_file)
    print('----read_from_json----')
    print('json_url:',j)
    return j

data = {'people':[{'name':'Superman','website':'superman.com','from':'Mars'}]}

def dump_json(dic_data):
    j_file = json.dumps(dic_data,indent=4)
    print('----dump_json----')
    print(f'Will output:{j_file}')
    return j_file


if __name__ == '__main__':
    read_from_json('1109_api/static/data/config_data.json')
    dump_json(data)