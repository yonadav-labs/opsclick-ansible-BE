{
    'name': 'nagios',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Application',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'server port',
            'type': 'Number',
            'default': 80
        },
    ]
}
