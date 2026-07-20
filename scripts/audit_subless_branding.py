#!/usr/bin/env python3
"""Fail when user-facing Nuvio branding is reintroduced into Subless TV."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STRING_RE = re.compile(r'<string\s+name="([^"]+)"[^>]*>(.*?)</string>', re.I | re.S)
BRAND_RE = re.compile(
    r"NuvioTV|Nuvio TV|Nuvio|Nuvia|Nuvios|Nuviót|NUVİO|நுவியோ",
    re.I,
)

errors: list[str] = []

# Resource names retain historical identifiers for source compatibility; only values
# are user-visible and therefore audited.
for path in sorted((ROOT / "app/src/main/res").glob("values*/**/*.xml")):
    text = path.read_bytes().decode("utf-8")
    for match in STRING_RE.finditer(text):
        key, value = match.groups()
        if BRAND_RE.search(value):
            errors.append(f"{path.relative_to(ROOT)}: string {key!r} still exposes Nuvio branding")

public_patterns: dict[str, tuple[str, ...]] = {
    "app/build.gradle.kts": (
        'buildConfigField("String", "GITHUB_OWNER", "\"tapframe\"")',
        'buildConfigField("String", "GITHUB_REPO", "\"NuvioTV\"")',
        'file("../nuviotv.jks")',
    ),
    ".github/workflows/beta-release.yml": (
        "secrets.NUVIO_RELEASE_KEYSTORE_BASE64",
        "$RUNNER_TEMP/nuviotv.jks",
        "CI_USE_DEBUG_SIGNING=true",
    ),
    "scripts/release_beta.py": (
        'APK_DIR = ROOT / "app" / "build" / "outputs" / "apk" / "release"',
        '["./gradlew", "app:assembleRelease"]',
        '"app-universal-release.apk"',
    ),
    "app/src/main/java/com/nuvio/tv/ui/screens/settings/AboutScreen.kt": (
        "tapframe.github.io/NuvioStreaming",
    ),
    "app/src/main/java/com/nuvio/tv/ui/screens/account/AuthQrSignInScreen.kt": (
        "https://nuvio.tv/terms",
    ),
    "app/src/main/java/com/nuvio/tv/ui/screens/settings/LicensesAttributionsScreen.kt": (
        "https://github.com/NuvioMedia/NuvioTV",
    ),
    "app/src/main/java/com/nuvio/tv/ui/screens/library/LibraryScreen.kt": (
        '-> "NUVIO"',
    ),
    "app/src/main/java/com/nuvio/tv/ui/screens/settings/DebridSettingsViewModel.kt": (
        'startDeviceAuthorization("Nuvio")',
    ),
    "app/src/main/java/com/nuvio/tv/core/server/AddonWebPage.kt": (
        'alt="NuvioTV"',
        "a.download = 'nuvio-collections.json'",
    ),
    "app/src/main/java/com/nuvio/tv/core/server/RepositoryWebPage.kt": ('alt="NuvioTV"',),
    "app/src/main/java/com/nuvio/tv/core/server/DebridFormatterWebPage.kt": (
        '?: "NuvioTV"',
        'alt="NuvioTV"',
    ),
    "app/src/main/java/com/nuvio/tv/core/server/StreamBadgeWebPage.kt": ('?: "NuvioTV"',),
    "app/src/main/java/com/nuvio/tv/core/di/NetworkModule.kt": ('"Nuvio/$version"',),
    "app/src/main/java/com/nuvio/tv/core/di/SupabaseModule.kt": ('"NuvioTV/${',),
    "app/src/full/java/com/nuvio/tv/core/plugin/PluginManager.kt": ('"NuvioTV/1.0"',),
    "app/src/full/java/com/nuvio/tv/core/plugin/cloudstream/ExternalRepoParser.kt": ('"NuvioTV/1.0"',),
    "app/src/full/java/com/nuvio/tv/core/plugin/cloudstream/ExternalExtensionLoader.kt": ('"NuvioTV/1.0"',),
    "app/src/main/java/com/nuvio/tv/ui/components/LoadingIndicator.kt": ("R.raw.nuvio_loading_indicator",),
    "README.md": ("NuvioTV", "Nuvio TV", "tapframe/NuvioTV", "nuvioapp.space"),
    "CONTRIBUTING.md": ("NuvioTV", "Nuvio TV"),
    ".github/PULL_REQUEST_TEMPLATE.md": ("NuvioTV", "Nuvio TV"),
}

for relative, forbidden in public_patterns.items():
    path = ROOT / relative
    if not path.exists():
        errors.append(f"Missing audited file: {relative}")
        continue
    text = path.read_text(encoding="utf-8")
    for token in forbidden:
        if token in text:
            errors.append(f"{relative}: contains forbidden public token {token!r}")

old_raw = ROOT / "app/src/main/res/raw/nuvio_loading_indicator.json"
if old_raw.exists():
    errors.append(f"Legacy branded runtime resource still exists: {old_raw.relative_to(ROOT)}")

if errors:
    print("Subless branding audit failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print("Subless branding audit passed: no user-facing Nuvio branding detected.")
