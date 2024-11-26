"""
Read data from a json file.
parse the json
save the parsed data in a file

"""
import json

with open('package.json', 'r') as read_data:
    json_data = read_data.read()
    print(json_data)


print("\n\n")
data = json.loads(json_data)
print(data)


question = data['quiz']['sport']['q1']['question']
answer = data['quiz']['sport']['q1']['answer']

print(question, answer)
with open('write_JsonData', 'w') as write_data:
    write_data.write(f"question: {question}\nanswer: {answer}")

with open('write_JsonData', 'r') as read_data:
    data = read_data.read()
    print(data)

