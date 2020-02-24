# apt

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/apt/status.svg)](https://cloud.drone.io/rolehippie/apt)

Ansible role to configure apt

## Table of content

* [Default Variables](#default-variables)
  * [apt_enable_backports](#apt_enable_backports)
  * [apt_enable_multiverse](#apt_enable_multiverse)
  * [apt_enable_universe](#apt_enable_universe)
  * [apt_force_update](#apt_force_update)
  * [apt_periodic_config](#apt_periodic_config)
  * [apt_unattended_upgrade_allowed_origins](#apt_unattended_upgrade_allowed_origins)
  * [apt_unattended_upgrade_dev_release](#apt_unattended_upgrade_dev_release)
  * [apt_unattended_upgrade_download_limit](#apt_unattended_upgrade_download_limit)
  * [apt_unattended_upgrade_mail_on_error_only](#apt_unattended_upgrade_mail_on_error_only)
  * [apt_unattended_upgrade_mail_to](#apt_unattended_upgrade_mail_to)
  * [apt_unattended_upgrade_package_blacklist](#apt_unattended_upgrade_package_blacklist)
  * [apt_unattended_upgrade_remove_unused_deps](#apt_unattended_upgrade_remove_unused_deps)
  * [apt_unattended_upgrade_remove_unused_kernel](#apt_unattended_upgrade_remove_unused_kernel)
  * [apt_unattended_upgrade_syslog_enabled](#apt_unattended_upgrade_syslog_enabled)
  * [apt_unattended_upgrade_syslog_facility](#apt_unattended_upgrade_syslog_facility)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### apt_enable_backports

Enable backports repositories

#### Default value

```YAML
apt_enable_backports: true
```

### apt_enable_multiverse

Enable multiverse repositories

#### Default value

```YAML
apt_enable_multiverse: true
```

### apt_enable_universe

Enable universe repositories

#### Default value

```YAML
apt_enable_universe: true
```

### apt_force_update

Force apt cache update

#### Default value

```YAML
apt_force_update: false
```

### apt_periodic_config

Set apt options for daily tasks

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

Automatically upgrade packages from these pairs

#### Default value

```YAML
apt_unattended_upgrade_allowed_origins:
  - ${distro_id}:${distro_codename}
  - ${distro_id}:${distro_codename}-security
  - ${distro_id}ESM:${distro_codename}
```

### apt_unattended_upgrade_dev_release

Automatically upgrade Ubuntu development releases

#### Default value

```YAML
apt_unattended_upgrade_dev_release: false
```

### apt_unattended_upgrade_download_limit

Use apt bandwidth limit feature, limits the download speed

#### Default value

```YAML
apt_unattended_upgrade_download_limit:
```

#### Example usage

```YAML
apt_unattended_upgrade_download_limit: '70'
```

### apt_unattended_upgrade_mail_on_error_only

Send emails only if an unattended upgrade fails

#### Default value

```YAML
apt_unattended_upgrade_mail_on_error_only: true
```

### apt_unattended_upgrade_mail_to

Send email to this address for problems or packages upgrades

#### Default value

```YAML
apt_unattended_upgrade_mail_to: root
```

#### Example usage

```YAML
apt_unattended_upgrade_mail_to: user@example.com
```

### apt_unattended_upgrade_package_blacklist

List of packages to not update

#### Default value

```YAML
apt_unattended_upgrade_package_blacklist: []
```

#### Example usage

```YAML
apt_unattended_upgrade_package_blacklist:
  - nvim
  - nginx
```

### apt_unattended_upgrade_remove_unused_deps

Do automatic removal of new unused dependencies after the upgrade

#### Default value

```YAML
apt_unattended_upgrade_remove_unused_deps: true
```

### apt_unattended_upgrade_remove_unused_kernel

Remove unused installed kernel-related packages automatically

#### Default value

```YAML
apt_unattended_upgrade_remove_unused_kernel: false
```

### apt_unattended_upgrade_syslog_enabled

#### Default value

```YAML
apt_unattended_upgrade_syslog_enabled: true
```

### apt_unattended_upgrade_syslog_facility

Specify syslog facility

#### Default value

```YAML
apt_unattended_upgrade_syslog_facility: daemon
```

## Dependencies

None.

## License

Apache-2.0

## Author

Thomas Boerger
