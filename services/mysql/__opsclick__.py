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
            # (required, required, required, optional)
            # ('ansible_variable_name', 'text to show in UI', 'field type', 'default value')
            ('root_pass', 'Root password', 'Password'),
            ('port', 'Mysql port', 'Number', 3306),
            ('db_name', 'Database name', 'String'),
            ('db_user', 'Database username', 'String'),
            ('db_pass', 'Database username password', 'Password')
    ]
}
