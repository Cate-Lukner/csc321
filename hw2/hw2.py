import netifaces as ni
import ipaddress

def get_interfaces():
    """Return a list of all the interfaces on this host

    Args: None

    Returns: (list) List of interfaces for this host
    """
    return ni.interfaces()

def get_mac(interface: str):
    """For the given interface string, return the MAC address as a
    string

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (str) MAC address
    """
    addrs = ni.ifaddresses(interface)
    return addrs[ni.AF_LINK]

def get_ips(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 address objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('192.168.65.48'),
       'v6': ipaddress.IPv6Address('fe80::14e1:8686:e720:57a')}
    """
    # get interface addresses
    addrs = ni.ifaddresses(interface)

    # Both none
    if addrs.get(ni.AF_INET6) == None and addrs.get(ni.AF_INET) == None:
      return None
    # Only INET6 none
    elif addrs.get(ni.AF_INET6) == None:
      ipv4 = addrs.get(ni.AF_INET)[0]['addr']
      return {'v4': ipaddress.IPv4Address(ipv4),
              'v6': None} 
    # Both valid
    else:
      ipv4 = addrs.get(ni.AF_INET)[0]['addr']
      ipv6_scope_id = addrs.get(ni.AF_INET6)[0]['addr']
      ipv6 = ipv6_scope_id.split('%', 1)[0]

      return {'v4': ipaddress.IPv4Address(ipv4),
              'v6': ipaddress.IPv6Address(ipv6)} 

def get_netmask(interface: str):
    """For the given interface string, return a dictionary with the
    IPv4 and IPv6 netmask objects (as IPv4/v6Address objects) for that
    interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('255.255.255.0'),
       'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')}
    """
    # get interface addresses
    addrs = ni.ifaddresses(interface)

    # Both none
    if addrs.get(ni.AF_INET6) == None and addrs.get(ni.AF_INET) == None:
      return None
    # Only INET6 none
    elif addrs.get(ni.AF_INET6) == None:
      ipv4 = addrs.get(ni.AF_INET)[0]['netmask']
      return {'v4': ipaddress.IPv4Address(ipv4),
              'v6': None} 
    # Both valid
    else:
      ipv4 = addrs.get(ni.AF_INET)[0]['netmask']
      ipv6_scope_id = addrs.get(ni.AF_INET6)[0]['netmask']
      ipv6 = ipv6_scope_id.split('/', 1)[0]

      return {'v4': ipaddress.IPv4Address(ipv4),
              'v6': ipaddress.IPv6Address(ipv6)} 




def get_network(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 network objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Network('192.168.65.0/24'),
       'v6': ipaddress.IPv6Network('fe80::/64')}
    """
    # get interface addresses
    addrs = ni.ifaddresses(interface)

    # Both none
    if addrs.get(ni.AF_INET6) == None and addrs.get(ni.AF_INET) == None:
      return None
    # Only INET6 none
    elif addrs.get(ni.AF_INET6) == None:
      ipv4 = addrs.get(ni.AF_INET)[0]['addr']
      return {'v4': ipaddress.IPv4Address(ipv4),
              'v6': None} 
    # Both valid
    else:
      ipv4 = addrs.get(ni.AF_INET)[0]['addr']
      ipv6_scope_id = addrs.get(ni.AF_INET6)[0]['addr']
      ipv6 = ipv6_scope_id.split('%', 1)[0]

      return {'v4': ipaddress.IPv4Network(ipv4),
              'v6': ipaddress.IPv6Network(ipv6)} 

