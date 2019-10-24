import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_apt_update(host):
    update = host.run("apt update")

    assert update.rc == 0


def test_apt_unattended_upgrade(host):
    uu = host.run("unattended-upgrade --dry-run")

    assert uu.rc == 0
