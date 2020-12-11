from application import app
application = app

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://08e6ca2861ee47569cb0ecaf13725c13@o489932.ingest.sentry.io/5553009",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)


if __name__ == "__main__":
    app.run()