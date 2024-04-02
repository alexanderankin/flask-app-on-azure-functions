import azure.functions as func
from FlaskApp import app

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the WSGI handler.
    """
    func.buffer = False
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)