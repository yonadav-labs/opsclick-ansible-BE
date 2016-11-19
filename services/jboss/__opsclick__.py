{
    'name': 'jboss',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'JBoss Application Server',
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
        {
            'name': 'jboss_pass',
            'label': 'admin password',
            'type': 'Password',
        },
    ]
}
