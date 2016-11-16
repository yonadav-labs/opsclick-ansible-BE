{
    'name': 'wildfly',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Java Application Server',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'server port',
            'type': 'Number',
            'default': 8080
        },
    ]
}
