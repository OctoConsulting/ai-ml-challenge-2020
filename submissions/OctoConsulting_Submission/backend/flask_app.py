from flask import Flask
import clause_parsing

app = Flask(__name__)

@app.route("/")
def hello():
    return clause_parsing.extract_all_clauses('hello.none')

if __name__ == '__main__':
    app.run()