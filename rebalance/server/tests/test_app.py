import morepath
import server

from webtest import TestApp as Client


def test_root():
    morepath.scan(server)
    morepath.commit(server.App)

    client = Client(server.App())
    root = client.get('/')

    assert root.status_code == 200
    assert len(root.json['greetings']) == 2
