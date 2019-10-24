# apt

[![Build Status](https://drone.owncloud.services/api/badges/ansible/apt/status.svg)](https://drone.owncloud.services/ansible/apt)


Ansible role to configure apt

## Table of content

* [Default Variables](#default-variables)
  * [apt_enable_universe](#apt_enable_universe)
  * [apt_enable_multiverse](#apt_enable_multiverse)
  * [apt_enable_backports](#apt_enable_backports)
  * [apt_force_update](#apt_force_update)
  * [apt_periodic_config](#apt_periodic_config)
  * [apt_unattended_upgrade_allowed_origins](#apt_unattended_upgrade_allowed_origins)
  * [apt_unattended_upgrade_package_blacklist](#apt_unattended_upgrade_package_blacklist)
  * [apt_unattended_upgrade_dev_release](#apt_unattended_upgrade_dev_release)
  * [apt_unattended_upgrade_mail_to](#apt_unattended_upgrade_mail_to)
  * [apt_unattended_upgrade_mail_on_error_only](#apt_unattended_upgrade_mail_on_error_only)
  * [apt_unattended_upgrade_remove_unused_kernel](#apt_unattended_upgrade_remove_unused_kernel)
  * [apt_unattended_upgrade_remove_unused_deps](#apt_unattended_upgrade_remove_unused_deps)
  * [apt_unattended_upgrade_syslog_enabled](#apt_unattended_upgrade_syslog_enabled)
  * [apt_unattended_upgrade_syslog_facility](#apt_unattended_upgrade_syslog_facility)
  * [apt_unattended_upgrade_download_limit](#apt_unattended_upgrade_download_limit)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### apt_enable_universe

#### Default value

```YAML
apt_enable_universe: true
```

### apt_enable_multiverse

#### Default value

```YAML
apt_enable_multiverse: true
```

### apt_enable_backports

#### Default value

```YAML
apt_enable_backports: true
```

### apt_force_update

#### Default value

```YAML
apt_force_update: false
```

### apt_periodic_config

Set apt options for daily tasks. If you are looiking for all possible configuration options, have a look at `/usr/lib/apt/apt.systemd.daily`.

#### Default value

```YAML
apt_periodic_config:
  - name: Update-Package-Lists
    value: 1
  - name: Download-Upgradeable-Packages
    value: 0
  - name: AutocleanInterval
    value: 1
  - name: Unattended-Upgrade
    value: 0
```

### apt_unattended_upgrade_allowed_origins

Automatically upgrade packages from these (origin:archive) pairs.

#### Default value

```YAML
apt_unattended_upgrade_allowed_origins:
  - ${distro_id}:${distro_codename}
  - ${distro_id}:${distro_codename}-security
  - ${distro_id}ESM:${distro_codename}
```

### apt_unattended_upgrade_package_blacklist

List of packages to not update (regexp are supported).

#### Default value

```YAML
apt_unattended_upgrade_package_blacklist: []
```

#### Example usage

```YAML
apt_unattended_upgrade_package_blacklist:
  - vim
  - nginx
```

### apt_unattended_upgrade_dev_release

This option will controls whether the development release of Ubuntu will be upgraded automatically.

#### Default value

```YAML
apt_unattended_upgrade_dev_release: false
```

### apt_unattended_upgrade_mail_to

Send email to this address for problems or packages upgrades If empty or unset then no email is sent, make sure that you have a working mail setup on your system. A package that provides `mailx` must be installed.

#### Default value

```YAML
apt_unattended_upgrade_mail_to: root
```

#### Example usage

```YAML
apt_unattended_upgrade_mail_to: user@example.com
```

### apt_unattended_upgrade_mail_on_error_only

Set this value to "true" to get emails only on errors.

#### Default value

```YAML
apt_unattended_upgrade_mail_on_error_only: false
```

### apt_unattended_upgrade_remove_unused_kernel

Remove unused automatically installed kernel-related packages (kernel images, kernel headers and kernel version locked tools).

#### Default value

```YAML
apt_unattended_upgrade_remove_unused_kernel: false
```

### apt_unattended_upgrade_remove_unused_deps

Do automatic removal of new unused dependencies after the upgrade (equivalent to apt-get autoremove).

#### Default value

```YAML
apt_unattended_upgrade_remove_unused_deps: true
```

### apt_unattended_upgrade_syslog_enabled

#### Default value

```YAML
apt_unattended_upgrade_syslog_enabled: true
```

### apt_unattended_upgrade_syslog_facility

Specify syslog facility.

#### Default value

```YAML
apt_unattended_upgrade_syslog_facility: daemon
```

### apt_unattended_upgrade_download_limit

Use apt bandwidth limit feature. The example limits the download speed to 70kb/sec.

#### Default value

```YAML
apt_unattended_upgrade_download_limit: _unset_
```

#### Example usage

```YAML
apt_unattended_upgrade_download_limit: '70'
```

## Dependencies

None.

## License

Apache-2.0

## Author

Thomas Boerger
