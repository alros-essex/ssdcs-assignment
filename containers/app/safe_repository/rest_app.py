from flask import Flask

class RestApp():

    def run(self):
        app = Flask('safe repository')

        @app.route("/")
        def hello():
            return "hello world!"
        
        app.run(host="0.0.0.0")