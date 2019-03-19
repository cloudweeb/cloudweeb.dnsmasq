import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_packages(host):
    p = host.package("dnsmasq")
    assert p.is_installed


def test_service(host):
    s = host.service("dnsmasq")
    assert s.is_running


@pytest.mark.parametrize("socket", [
    "udp://127.0.0.1:53",
    "tcp://127.0.0.1:53"
])
def test_socket(host, socket):
    s = host.socket(socket)
    assert s.is_listening
