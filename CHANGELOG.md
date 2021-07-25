# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/corneliusroemer/autovpn/compare/v0.2.2...HEAD)

## [0.2.2](https://github.com/corneliusroemer/autovpn/compare/v0.2.1...v0.2.2) - 2021-07-25
### Added
- Custom path for vpn binary

### Fixed
- If `~/.autovpnconfig` not present, it's created
- If `~/.autovpnconfig` not present, user is prompted to configure

## [0.2.1](https://github.com/corneliusroemer/autovpn/compare/v0.2.0...v0.2.1) - 2021-07-24
### Changed
- Minimum Python version is 3.7 not 3.6

## [0.2.0](https://github.com/corneliusroemer/autovpn/compare/v0.1.0...v0.2.0) - 2021-07-24
### Added
- Configuration through the command line using `autovpn configure`

### Changed
- Moved the configuration file from `~/.vpnconfig` to `~/.autovpnconfig`
