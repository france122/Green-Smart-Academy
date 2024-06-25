from flask import Flask, request, render_template
import csv

app = Flask(__name__)

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def search_data(data, keyword):
    results = []
    keyword = keyword.lower()
    for row in data:
        if (keyword in row['Title-题名'].lower() or
            keyword in row['Author-作者'].lower() or
            keyword in row['Organ-单位'].lower() or
            keyword in row['Source-文献来源'].lower() or
            keyword in row['Keyword-关键词'].lower()):
            results.append(row)
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        data = read_csv('static/data.csv')
        results = search_data(data, query)
    else:
        results = []
    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
