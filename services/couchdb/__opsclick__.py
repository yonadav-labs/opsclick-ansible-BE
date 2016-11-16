{
    'name': 'couchdb',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Database',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'Couchdb port',
            'type': 'Number',
            'default': 5984
        },
        {
            'name': 'couchdb_user',
            'label': 'Database User',
            'type': 'String',
        },
        {
            'name': 'couchdb_password',
            'label': 'Database Password',
            'type': 'Password',
        }    
    ]
}
