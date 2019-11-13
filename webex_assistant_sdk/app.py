from flask import Flask
from mindmeld import Application

from .server import create_agent_server


class AgentApplication(Application):
    """
    An implementation of AgentApplication using AgentServer.
    """

    def __init__(self, import_name, *, secret, private_key, **kwargs):
        super().__init__(import_name, **kwargs)
        self.secret = secret
        self.private_key = private_key

    def lazy_init(self, nlp=None):
        Application.lazy_init(self, nlp)
        self._server = create_agent_server(self.app_manager, self.secret, self.private_key)

    @property
    def web_app(self) -> Flask:
        return self._server
