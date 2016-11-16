{
    'name': 'tomcat',
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
            'label': 'Tomcat port',
            'type': 'Number',
            'default': 8080
        },
        {
            'name': 'admin_pass',
            'label': 'Tomcat admin password',
            'type': 'Password',
        }    
    ]
}
