{
    'name': 'wordpress',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Application',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'wordpress port',
            'type': 'Number',
            'default': 80
        },
        {
            'name': 'ssl_port',
            'label': 'wordpress ssl port',
            'type': 'Number',
            'default': 443
        },
        {
            'name': 'app_name',
            'label': 'wordpress application name',
            'type': 'String',
            'default': 'wordpress.local'
        },
        {
            'name': 'apache_svralias',
            'label': 'wordpress apache svralias',
            'type': 'String',
            'default': 'www.wordpress.com localhost'
        },
        {
            'name': 'mysql_server',
            'label': 'MySql Server',
            'type': 'String',
            'default': 'localhost'
        },
        {
            'name': 'mysql_pass',
            'label': 'wordpress mysql password',
            'type': 'Password',
        },
        {
            'name': 'mysql_db',
            'label': 'MySql Database name',
            'type': 'String',
            'default': 'wordpress'
        },
        {
            'name': 'app_user',
            'label': 'wordpress application user',
            'type': 'String',
            'default': 'admin'
        },
        {
            'name': 'app_pass',
            'label': 'wordpress application password',
            'type': 'Password'
        },
        {
            'name': 'wp_key',
            'label': 'wordpress password',
            'type': 'Password'
        },
        # {
        #     'name': 'env',
        #     'label': 'environment',
        #     'type': 'String',
        #     'default': 'production'
        # },
        # {
        #     'name': 'termtag',
        #     'label': 'tags',
        #     'type': 'String',
        #     'default': 'wordpress'
        # }
    ]
}
