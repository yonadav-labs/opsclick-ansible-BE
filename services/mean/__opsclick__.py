{
    'name': 'mean',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Javascript Development Stack',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'http_port',
            'label': 'HTTP port',
            'type': 'Number',
            'default': 80
        },
        {
            'name': 'https_port',
            'label': 'HTTPS port',
            'type': 'Number',
            'default': 443
        },
        {
            'name': 'meanjs_port',
            'label': 'MEAN.JS server port',
            'type': 'Number',
            'default': 3000
        },
    ]
}
