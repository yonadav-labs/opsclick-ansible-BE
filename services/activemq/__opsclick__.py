{
    'name': 'activemq',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Messaging Service',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'activemq port',
            'type': 'Number',
            'default': 8161
        },
        {
            'name': 'activemq_min_memory',
            'label': 'activemq minimum memory',
            'type': 'Number',
            'default': 1024
        },
        {
            'name': 'activemq_max_memory',
            'label': 'activemq maximum memory',
            'type': 'Number',
            'default': 4096
        },       
        # {
        #     'name': 'activemq_admin_login',
        #     'label': 'activemq admin user',
        #     'type': 'String',
        #     'default': 'admin'
        # },
        # {
        #     'name': 'activemq_admin_password',
        #     'label': 'activemq admin password',
        #     'type': 'Password'
        # }
    ]
}
