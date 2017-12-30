import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root' or f.group == 'wheel'


def test_service_running(host):
    # update for test on freebsd
    os_version = host.system_info.distribution
    if os_version == "freebsd":
        minion_service = host.service('salt_minion')
    else:
        minion_service = host.service('salt-minion')
    assert minion_service.is_running


def test_minion_configuration(host):
    os_version = host.system_info.distribution
    os_path = ""
    if os_version == "freebsd":
        os_path = "/usr/local/etc/salt/minion"
    else:
        os_path = "/etc/salt/minion"
    minion_config = host.file(os_path)
    assert minion_config.contains('salt.example.com')
