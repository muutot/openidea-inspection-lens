# Inspection Lens — inline diagnostics for OpenIDEA

Draws each diagnostic at the end of the line it belongs to, coloured by
severity, with a native hover tooltip — the way JetBrains' Inspection Lens and
VS Code's Error Lens do it.

![Line-end annotations between the code and the inline blame](https://raw.githubusercontent.com/muutot/openidea/pr-assets/3103/lens-editor.png)

## Install

Settings › Plugins › Install Plugin from Disk… and pick this folder (it needs
`plugin.toml` and `dist/plugin.wasm`), or install the released package from the
marketplace once it is listed.

Grants: `project.read`, `events`, `storage` — all low risk. The page appears
under Settings › Plugins › Inspection Lens, one level, with no nested folder.

## What it does

- Reads the host's diagnostics snapshot (`host::problems(None)`), one entry per
  file and producer: language servers, builds, spelling and other plugins.
- Groups them by line and draws one annotation per line: the first message, then
  `· +N more`; the hover carries every message (or the full one with tool/rule/
  location, depending on the hover mode).
- Places the text at the line end in the editor's UTF-16 columns, so it lands
  after the code even on wrapped lines. The host renders it out of flow: it does
  not stretch the line, and it steps past the git hint and before the inline
  blame.
- Refreshes on `file-opened`, `file-saved`, `editor-focused`, `file-closed`,
  `settings-changed` and `problems-changed`, and on the _Inspection Lens:
  Refresh_ command (Search Everywhere).

## Settings

The page mirrors PyCharm's Inspection Lens: Appearance / Behavior / Shown
Severities.

| Group            | Setting                | Effect                                                                                                                 |
| ---------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Appearance       | Use editor font        | Severity colours on; off draws every message muted.                                                                     |
| Appearance       | Max description length | Truncate long messages with an ellipsis (0 = unlimited).                                                                |
| Behavior         | Hover mode             | `Disabled`, or one of PyCharm's two click modes: the tooltip with tool, rule id and related locations, or the message alone. |
| Shown Severities | 11 categories          | Agent / Errors / Warnings / Debugger suggestions / Information / Weak warnings / Server problems / Syntax errors / Typos / Style suggestions / Other — one category per diagnostic, with an example in its own style. |

The text takes its colour from the Color Scheme attributes of the same kind
(Settings › Editor › Color Scheme › General › Errors and Warnings), so editing
Error, Warning, Weak warning or Typo there recolours both the code and its
annotation.

## Limitations

- The host's decoration API has no click binding and no font control: the two
  hover modes only change what the tooltip carries, and _Use editor font_
  switches between severity colours and muted text.
- Plugins cannot write their own settings, so the page's Reset discards staged
  edits only.
- Needs plugin API 1.8 (`engines.openidea = "^1.8"`): the `problems-changed`
  event and the host-owned diagnostics snapshot it reads. The 1.8 release is
  [l0ng-ai/openidea#3103](https://github.com/l0ng-ai/openidea/pull/3103); the
  0.1.0 package was built before it shipped and installs only on a build that
  carries it.
- Remote projects: plugins see the Problems snapshot of the machine they run on.

## Build

```sh
openidea-plugin build .            # dist/plugin.wasm (needs the wasm32-wasip2 target)
openidea-plugin check .            # what the IDE validates on install
```

`openidea-plugin` ships with OpenIDEA releases; `cargo install --locked --git
https://github.com/l0ng-ai/openidea ide-host --bin openidea-plugin` builds it
from source.

The component is compiled against the released SDK tag in `Cargo.toml`
(`openidea-plugin = { git = "…", tag = "v0.1.44" }`).

## Publish

```sh
openidea-plugin keygen muutot.key                      # once; keep the file secret
openidea-plugin pack . --key muutot.key --publisher muutot
```

Attach `muutot.inspection-lens-<version>.oiplugin` to a release here, then add
the version, URL and SHA-256 to the registry
([l0ng-ai/openidea-plugins](https://github.com/l0ng-ai/openidea-plugins)).
