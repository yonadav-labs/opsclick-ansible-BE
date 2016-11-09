{
    'name': 'apache',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Web Server',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'Apache port',
            'type': 'Number',
            'default': 80
        },
        {
            'name': 'ssl_port',
            'label': 'Apache ssl port',
            'type': 'Number',
            'default': 443
        }    
    ]
}
