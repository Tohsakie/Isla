#!/usr/bin/env python3

import connexion
import API.databases.postgres_connection as db


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.add_api('openapi.yaml',
                arguments={'title': 'Isla - Token API'},
                pythonic_params=True)

    flask_app = app.app

    db.init()

    app.run(port=8081, host="0.0.0.0")


if __name__ == '__main__':
    main()
