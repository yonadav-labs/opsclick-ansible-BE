{
    'name': 'digitalocean',
    'author': 'Luis Alfredo da Silva',
    'type': 'cloud',
    'version': '1.0',
    'fields': [
        {
            'name': 'droplets',
            'label': 'Name of the droplets',
            'type': 'List(String)'
        },
        {
            'name': 'size',
            'label': 'Size of the droplets',
            'type': 'String'
        },
        {
            'name': 'image',
            'label': 'Name of the image',
            'type': 'List(String)'
        },
        {
            'name': 'region',
            'label': 'Name of the region',
            'type': 'String'
        },
        {
            'name': 'ssh_pub_keys',
            'label': 'SSH key',
            'type': 'String'
        },
        {
            'name': 'access_key',
            'label': 'DigitalOcean API Access Key',
            'type': 'String'
        }
    ]
}
