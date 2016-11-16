{
    'name': 'elasticsearch',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Search Engine',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'server port',
            'type': 'Number',
            'default': 9200
        },
    ]
}
