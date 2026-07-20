<div align="center">

  <img src="assets/brand/app_logo_wordmark.png" alt="Subless TV" width="300" />
  <br />
  <br />

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![License][license-shield]][license-url]

  <p>
    A modern Android TV media player powered by the Stremio addon ecosystem.
    <br />
    Stremio Addon ecosystem • Android TV optimized • Playback-focused experience
  </p>

</div>

## About

Subless TV is a modern media player designed specifically for Android TV.

It acts as a client-side playback interface that can integrate with the Stremio addon ecosystem for content discovery and source resolution through user-installed extensions.

Built with Kotlin and optimized for a TV-first viewing experience.

## Installation

### Android TV

Download the latest APK from [GitHub Releases](https://github.com/ShiftAboveCtrl/SSMedia/releases/latest) and install on your Android TV device.

## Development

### Prerequisites

- Android Studio (latest version)
- JDK 11+
- Android SDK (API 29+)
- Gradle 8.0+

### Setup

```bash
git clone https://github.com/ShiftAboveCtrl/SSMedia.git
cd SSMedia
```

### Full Debug Build

```bash
./gradlew :app:compileFullDebugKotlin
./gradlew :app:assembleFullDebug
```

### Running on Emulator or Device

```bash
# Full debug build
./gradlew :app:assembleFullDebug

# Run on connected device
adb shell am start -n com.nuviodebug.com/com.nuvio.tv.MainActivity
```

## Legal & DMCA

Subless TV functions solely as a client-side interface for browsing metadata and playing media provided by user-installed extensions and/or user-provided sources. It is intended for content the user owns or is otherwise authorized to access.

Subless TV is not affiliated with any third-party extensions or content providers. It does not host, store, or distribute any media content.

For comprehensive legal information, including our full disclaimer, third-party extension policy, and DMCA/Copyright information, please visit our **[Legal & Disclaimer Page](https://sublessmedia.com/legal)**.

## Built With

* Kotlin
* Jetpack Compose & TV Material3
* ExoPlayer / Media3
* Hilt (Dependency Injection)
* Retrofit (Networking)
* Gradle

## Star History

<a href="https://www.star-history.com/#ShiftAboveCtrl/SSMedia&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ShiftAboveCtrl/SSMedia&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ShiftAboveCtrl/SSMedia&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ShiftAboveCtrl/SSMedia&type=date&legend=top-left" />
 </picture>
</a>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/ShiftAboveCtrl/SSMedia.svg?style=for-the-badge
[contributors-url]: https://github.com/ShiftAboveCtrl/SSMedia/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ShiftAboveCtrl/SSMedia.svg?style=for-the-badge
[forks-url]: https://github.com/ShiftAboveCtrl/SSMedia/network/members
[stars-shield]: https://img.shields.io/github/stars/ShiftAboveCtrl/SSMedia.svg?style=for-the-badge
[stars-url]: https://github.com/ShiftAboveCtrl/SSMedia/stargazers
[issues-shield]: https://img.shields.io/github/issues/ShiftAboveCtrl/SSMedia.svg?style=for-the-badge
[issues-url]: https://github.com/ShiftAboveCtrl/SSMedia/issues
[license-shield]: https://img.shields.io/github/license/ShiftAboveCtrl/SSMedia.svg?style=for-the-badge
[license-url]: http://www.gnu.org/licenses/gpl-3.0.en.html
