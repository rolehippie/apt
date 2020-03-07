import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_apt_update(host):
    run = host.run("apt update")
    assert run.rc == 0


def test_unattended_upgrade(host):
    run = host.run("unattended-upgrade --dry-run")
    assert run.rc == 0
