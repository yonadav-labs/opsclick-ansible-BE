{
    'name': 'rabbitmq',
    'type': 'service',
    'author': 'Andrew Thomas',
    'version': '0.1',
    'category': 'Messaging system',
    'clouds': [
        'digitalocean',
    ],
    'fields': [
        {
            'name': 'port',
            'label': 'management port',
            'type': 'Number',
            'default': 15672
        },
        {
            'name': 'user',
            'label': 'RabbitMQ default user',
            'type': 'String',
        },
        {
            'name': 'pass',
            'label': 'RabbitMQ default password',
            'type': 'Password'
        },
    ]
}
