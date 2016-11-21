{
    'name': 'lamp',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Web Development Stack',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'apache port',
            'type': 'Number',
            'default': 80
        },
        {
            'name': 'mysql_port',
            'label': 'mysql port',
            'type': 'Number',
            'default': 3306
        },
        {
            'name': 'mysql_pass',
            'label': 'mysql password',
            'type': 'Password',
        },
    ]
}
