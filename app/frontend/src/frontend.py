# - Fontend

from flask import Flask
import requests

app = Flask(__name__)

def getForwardHeaders(request):
    headers = {}

    # x-b3-*** headers can be populated using the OpenTelemetry span
    ctx = propagator.extract(carrier={k.lower(): v for k, v in request.headers})
    propagator.inject(headers, ctx)

    # ...

        incoming_headers = ['x-request-id',
        'x-ot-span-context',
        'x-datadog-trace-id',
        'x-datadog-parent-id',
        'x-datadog-sampling-priority',
        'traceparent',
        'tracestate',
        'x-cloud-trace-context',
        'grpc-trace-bin',
        'user-agent',
        'cookie',
        'authorization',
        'jwt',
    ]

    # ...

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val

    return headers

@app.route("/")
def call_backend():
    response = requests.get("http://backend-svc:5000")
    return f"Frontend got: {response.text}"

app.run(host="0.0.0.0", port=5000)
