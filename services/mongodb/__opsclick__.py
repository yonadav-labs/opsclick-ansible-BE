{
    'name': 'mongodb',
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
            'label': 'MongoDB port',
            'type': 'Number',
            'default': 27017
        },
        {
            'name': 'mongodb_user',
            'label': 'Database User',
            'type': 'String',
        },
        {
            'name': 'db_name',
            'label': 'Database Name',
            'type': 'String',
        },
        {
            'name': 'mongodb_pass',
            'label': 'Database Password',
            'type': 'Password',
        }    
    ]
}
