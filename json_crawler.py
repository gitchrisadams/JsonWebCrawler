from flask import Flask, render_template
import json 

app = Flask(__name__)

@app.route('/internet1', methods=['POST', 'GET'])
def internet1():
    with open('internet1.json', 'r') as internet1_json:
        internet1_dict = json.load(internet1_json);

    crawled_list = []
    skipped_list = []
    error_list = []
    all_addresses = []

    # Loop through and grab all address in all pages:
    for address_counter in range(len(internet1_dict['pages'])):
        all_addresses.append(internet1_dict['pages'][address_counter]['address'])

    # Loop through all pages:
    for counter in range(len(internet1_dict['pages'])):
        if internet1_dict['pages'][counter]['address'] not in crawled_list:
            crawled_list.append(internet1_dict['pages'][counter]['address'])
        for link in internet1_dict['pages'][counter]['links']:
            if link in crawled_list and link not in skipped_list:
                skipped_list.append(link)
            if link not in all_addresses:
                error_list.append(link)

    print('Success: ', crawled_list)
    print('Skipped: ', skipped_list)
    print('Error: ', error_list)
    return render_template('internet1.html', crawled_list=crawled_list, skipped_list=skipped_list, error_list=error_list)

@app.route('/internet2', methods=['POST', 'GET'])
def internet2():
    with open('internet2.json', 'r') as internet1_json:
        internet1_dict = json.load(internet1_json);

    crawled_list = []
    skipped_list = []
    error_list = []
    all_addresses = []

    # Loop through and grab all address in all pages:
    for address_counter in range(len(internet1_dict['pages'])):
        all_addresses.append(internet1_dict['pages'][address_counter]['address'])

    # Loop through all pages:
    for counter in range(len(internet1_dict['pages'])):
        if internet1_dict['pages'][counter]['address'] not in crawled_list:
            crawled_list.append(internet1_dict['pages'][counter]['address'])
        for link in internet1_dict['pages'][counter]['links']:
            if link in crawled_list and link not in skipped_list:
                skipped_list.append(link)
            if link not in all_addresses:
                error_list.append(link)

    print('Success: ', crawled_list)
    print('Skipped: ', skipped_list)
    print('Error: ', error_list)
    return render_template('internet2.html', crawled_list=crawled_list, skipped_list=skipped_list, error_list=error_list)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)