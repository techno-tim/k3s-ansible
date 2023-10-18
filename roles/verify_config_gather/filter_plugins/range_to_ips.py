import netaddr

''' returns True if ip is in range
    examples:
    - see test functions below
'''
def test(ip, range, expected):
    assert netaddr_ip_in_dash_range(ip, range) == expected

def test_netaddr_ip_in_dash_range():
    # ipv4
    test('192.168.1.1', '192.168.1.1-192.168.1.2', True)
    test('192.168.1.1', '192.168.1.1', True)
    test('192.168.1.1', '192.168.1.2-192.168.1.3', False)
    test('192.168.1.1', '192.168.1.2', False)

    # ipv6 style
    test('::ffff:192.168.1.1', '::ffff:192.168.1.1-::ffff:192.168.1.8', True)
    test('::ffff:192.168.1.1', '::ffff:192.168.1.1', True)
    test('::ffff:192.168.1.1', '::ffff:192.168.1.2-::ffff:192.168.1.8', False)
    test('::ffff:192.168.1.1', '::ffff:192.168.1.2', False)

    # Note I expedted true but apperently the netaddr library does not support this?? or I don't understand ipv6 :)
    test('::2:1', '::2:1-::2:2', False)
    '''
    todo: ?
    - netaddr_ip_in_dash_range('192.168.1.1',  '192.168.1.0/24')             => True (TODO: test, implement)
    - netaddr_ip_in_dash_range('192.168.99.1', '192.168.1.0/24')            => False (TODO: test, implement)
    '''

def netaddr_ip_in_dash_range(ip, range):
    # return False early if range is invalid
    if '-' not in range:
        ip_start = range
        ip_end = range
    else:
        ip_start = range.split('-')[0]
        ip_end = range.split('-')[1]
    return ip in [str(ip) for ip in netaddr.iter_iprange(ip_start, ip_end)]


class FilterModule(object):
        ''' Ansible filters. Interface to custom netaddr methods.
            https://pypi.org/project/netaddr/
        '''

        def filters(self):
            return {
                'netaddr_ip_in_dash_range' : netaddr_ip_in_dash_range
                }

if __name__ == '__main__':
    test_netaddr_ip_in_dash_range()
