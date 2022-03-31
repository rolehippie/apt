# apt

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/apt) [![Testing Build](https://github.com/rolehippie/apt/workflows/testing/badge.svg)](https://github.com/rolehippie/apt/actions?query=workflow%3Atesting) [![Readme Build](https://github.com/rolehippie/apt/workflows/readme/badge.svg)](https://github.com/rolehippie/apt/actions?query=workflow%3Areadme) [![Galaxy Build](https://github.com/rolehippie/apt/workflows/galaxy/badge.svg)](https://github.com/rolehippie/apt/actions?query=workflow%3Agalaxy) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/apt)](https://github.com/rolehippie/apt/blob/master/LICENSE)

Ansible role to configure APT repositories and settings.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Default Variables](#default-variables)
  - [apt_enable_backports](#apt_enable_backports)
  - [apt_enable_multiverse](#apt_enable_multiverse)
  - [apt_enable_universe](#apt_enable_universe)
  - [apt_force_update](#apt_force_update)
  - [apt_general_url](#apt_general_url)
  - [apt_periodic_config](#apt_periodic_config)
  - [apt_redundant_configs](#apt_redundant_configs)
  - [apt_security_url](#apt_security_url)
  - [apt_unattended_upgrade_allowed_origins](#apt_unattended_upgrade_allowed_origins)
  - [apt_unattended_upgrade_dev_release](#apt_unattended_upgrade_dev_release)
  - [apt_unattended_upgrade_download_limit](#apt_unattended_upgrade_download_limit)
  - [apt_unattended_upgrade_mail_on_error_only](#apt_unattended_upgrade_mail_on_error_only)
  - [apt_unattended_upgrade_mail_to](#apt_unattended_upgrade_mail_to)
  - [apt_unattended_upgrade_package_blacklist](#apt_unattended_upgrade_package_blacklist)
  - [apt_unattended_upgrade_remove_unused_deps](#apt_unattended_upgrade_remove_unused_deps)
  - [apt_unattended_upgrade_remove_unused_kernel](#apt_unattended_upgrade_remove_unused_kernel)
  - [apt_unattended_upgrade_syslog_enabled](#apt_unattended_upgrade_syslog_enabled)
  - [apt_unattended_upgrade_syslog_facility](#apt_unattended_upgrade_syslog_facility)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

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

### apt_general_url

General URL of repositories changed by architecture

#### Default value

```YAML
apt_general_url:
  x86_64: http://archive.ubuntu.com/ubuntu
  aarch64: http://ports.ubuntu.com/ubuntu-ports
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

### apt_redundant_configs

List of redundant configs that gets deleted

#### Default value

```YAML
apt_redundant_configs:
  - 20auto-upgrades
```

### apt_security_url

Security URL of repositories changed by architecture

#### Default value

```YAML
apt_security_url:
  x86_64: http://security.ubuntu.com/ubuntu
  aarch64: http://ports.ubuntu.com/ubuntu-ports
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

## Discovered Tags

**_apt_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
