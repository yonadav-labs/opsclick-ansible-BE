{
    'name': 'nginx',
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
            'label': 'Nginx port',
            'type': 'Number',
            'default': 80
        },
        {
            'name': 'ssl_port',
            'label': 'Nginx ssl port',
            'type': 'Number',
            'default': 443
        }    
    ]
}
