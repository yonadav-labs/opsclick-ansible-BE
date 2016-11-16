{
    'name': 'postgresql',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Database',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'postgres_pass',
            'label': 'Postgres password',
            'type': 'Password',
        },
        {
            'name': 'port',
            'label': 'Postgresql port',
            'type': 'Number',
            'default': 5432
        },
        {
            'name': 'db_name',
            'label': 'Database name',
            'type': 'String',
        },
        {
            'name': 'db_user',
            'label': 'Database user',
            'type': 'String',
        },
        {
            'name': 'db_pass',
            'label': 'Database user password',
            'type': 'Password',
        },

    ]
}
