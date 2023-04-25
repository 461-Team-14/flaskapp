import yaml
from flask import Flask

with open('ECE 461 - Spring 2023 - Project 2_V2.3.4.yaml', encoding='utf-8') as file:
    spec = yaml.safe_load(file)

app = Flask(__name__)

for path, methods in spec['paths'].items():
    for method, operation in methods.items():
        def view_func():
            return operation['responses']['200']['description']
        
        app.add_url_rule(path, view_func=view_func, methods=[method.upper()])

if __name__ == '__main__':
    app.run()

