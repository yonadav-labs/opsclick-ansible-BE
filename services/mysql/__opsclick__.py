{
    'name': 'mysql',
    'type': 'service',
    'author': 'Luis Alfredo da Silva',
    'version': '0.1',
    'category': 'Database',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'root_pass',
            'label': 'Root password',
            'type': 'Password',
        },
        {
            'name': 'port',
            'label': 'Mysql port',
            'type': 'Number',
            'default': 3306
        },
        {
            'name': 'db_name',
            'label': 'Database name',
            'type': 'String',
        },
        {
            'name': 'db_user',
            'label': 'Database user',
            'type': 'String',
        },
        {
            'name': 'db_pass',
            'label': 'Database user password',
            'type': 'Password',
        },

    ]
}
