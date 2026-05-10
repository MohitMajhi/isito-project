from flask import Flask, request
from opentelemetry.propagate import extract, inject

app = Flask(__name__)


def get_forward_headers(req):
    headers = {}

    # Extract trace context from incoming request
    ctx = extract(carrier={k.lower(): v for k, v in req.headers})

    # Inject trace context into outgoing headers
    inject(headers, context=ctx)

    incoming_headers = [
        'x-request-id',
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

    for ihdr in incoming_headers:
        val = req.headers.get(ihdr)

        if val is not None:
            headers[ihdr] = val

    return headers


@app.route("/")
def hello():
    headers = get_forward_headers(request)

    return {
        "message": "Hello from Backend!",
        "forward_headers": headers
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)