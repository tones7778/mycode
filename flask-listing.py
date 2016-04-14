import flask
import subprocess
import time          #You don't need this. Just included it so you can see the output stream.

#Testing
app = flask.Flask(__name__)

@app.route('/hello')
def index():
    def inner():
        proc = subprocess.Popen(
            ['ls -l'],             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'

    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

app.run(debug=True, port=8080, host='0.0.0.0')