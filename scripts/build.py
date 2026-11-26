#!/usr/bin/env python3
"""Validate the skills in .agents/skills/ and package them.

Standard library only. Python 3.8+.

Usage:
    python3 scripts/build.py                 # validate, then build dist/<skill>.zip files
    python3 scripts/build.py --check         # validate only (used in CI)
    python3 scripts/build.py --install PATH  # validate, then copy skills into
                                             # PATH/.claude/skills/ for Claude Code

A full build also writes dist/marketing-skills-plugin.zip: one plugin file
(.claude-plugin/plugin.json + skills/) for Claude's plugin upload.

Each ZIP has the skill folder at its root (my-skill.zip -> my-skill/SKILL.md),
which is the layout Claude expects for custom skill uploads.
"""

import argparse
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / ".agents" / "skills"
DIST_DIR = ROOT / "dist"

# Portable frontmatter keys from the Agent Skills spec (agentskills.io/specification).
# allowed-tools is in the spec but experimental and unevenly supported, so this pack avoids it.
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata"}
REQUIRED_KEYS = {"name", "description"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED_WORDS = ("anthropic", "claude")
MAX_NAME = 64
MAX_DESCRIPTION = 200  # claude.ai upload limit; the open spec allows 1024
MAX_COMPATIBILITY = 500
MAX_BODY_LINES = 500
SKIP_NAMES = {".DS_Store", "__pycache__", "Thumbs.db"}


def parse_frontmatter(text):
    """Parse the small YAML subset used in SKILL.md frontmatter.

    Supports `key: value` pairs and one level of nested `key: value` pairs
    (for metadata). Returns (dict, body) or raises ValueError.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with a '---' frontmatter line")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise ValueError("frontmatter has no closing '---' line")

    data = {}
    current_map = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indented = raw[0] in " \t"
        if ":" not in raw:
            raise ValueError("cannot parse frontmatter line: %r" % raw)
        key, _, value = raw.strip().partition(":")
        key, value = key.strip(), _unquote(value.strip())
        if indented:
            if current_map is None:
                raise ValueError("unexpected indented line: %r" % raw)
            current_map[key] = value
        elif value == "":
            current_map = {}
            data[key] = current_map
        else:
            current_map = None
            data[key] = value
    body = "\n".join(lines[end + 1:])
    return data, body


def _unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def validate_skill(skill_dir):
    errors = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return ["missing SKILL.md"]
    try:
        meta, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [str(exc)]

    for key in sorted(REQUIRED_KEYS - meta.keys()):
        errors.append("missing required key '%s'" % key)
    for key in sorted(meta.keys() - ALLOWED_KEYS):
        errors.append("non-portable frontmatter key '%s'" % key)

    name = meta.get("name", "")
    if isinstance(name, str) and name:
        if len(name) > MAX_NAME:
            errors.append("name is %d chars (max %d)" % (len(name), MAX_NAME))
        if not NAME_RE.match(name):
            errors.append("name must be lowercase letters, digits and single hyphens")
        if name != skill_dir.name:
            errors.append("name '%s' does not match folder '%s'" % (name, skill_dir.name))
        for word in RESERVED_WORDS:
            if word in name:
                errors.append("name contains reserved word '%s'" % word)

    desc = meta.get("description", "")
    if isinstance(desc, str) and desc:
        if len(desc) > MAX_DESCRIPTION:
            errors.append("description is %d chars (max %d)" % (len(desc), MAX_DESCRIPTION))
        if "<" in desc or ">" in desc:
            errors.append("description must not contain angle brackets")
    elif "description" in meta:
        errors.append("description must be a non-empty string")

    compat = meta.get("compatibility")
    if isinstance(compat, str) and len(compat) > MAX_COMPATIBILITY:
        errors.append("compatibility is %d chars (max %d)" % (len(compat), MAX_COMPATIBILITY))

    if "metadata" in meta and not isinstance(meta["metadata"], dict):
        errors.append("metadata must be a map of string keys to string values")

    body_lines = len(body.splitlines())
    if body_lines > MAX_BODY_LINES:
        errors.append("body is %d lines (keep under %d)" % (body_lines, MAX_BODY_LINES))

    # Every file the body links to under references/, scripts/ or assets/ must exist.
    for ref in sorted(set(re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", body))):
        if not (skill_dir / ref).exists():
            errors.append("links to missing file '%s'" % ref)
    return errors


def skill_dirs():
    if not SKILLS_DIR.is_dir():
        sys.exit("No skills folder at %s" % SKILLS_DIR)
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))


def skill_files(skill_dir):
    for path in sorted(skill_dir.rglob("*")):
        if path.is_file() and not any(part in SKIP_NAMES for part in path.parts):
            yield path


def build_zip(skill_dir):
    DIST_DIR.mkdir(exist_ok=True)
    out = DIST_DIR / (skill_dir.name + ".zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in skill_files(skill_dir):
            arcname = Path(skill_dir.name) / path.relative_to(skill_dir)
            zf.write(path, arcname.as_posix())
    return out


def build_plugin_zip(dirs):
    """One ZIP with .claude-plugin/plugin.json at its root and skills under skills/."""
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    manifest.pop("skills", None)  # skills/ is the default location inside the plugin ZIP
    DIST_DIR.mkdir(exist_ok=True)
    out = DIST_DIR / (manifest["name"] + "-plugin.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(".claude-plugin/plugin.json", json.dumps(manifest, indent=2) + "\n")
        icon = ROOT / ".claude-plugin" / "icon.png"
        if icon.is_file():
            zf.write(icon, ".claude-plugin/icon.png")
        for extra in ("README.md", "LICENSE"):
            if (ROOT / extra).is_file():
                zf.write(ROOT / extra, extra)
        for d in dirs:
            for path in skill_files(d):
                zf.write(path, (Path("skills") / d.name / path.relative_to(d)).as_posix())
    return out


def install(skill_dir, target_root):
    dest = Path(target_root).expanduser().resolve() / ".claude" / "skills" / skill_dir.name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(skill_dir, dest, ignore=shutil.ignore_patterns(*SKIP_NAMES))
    return dest


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="validate only, build nothing")
    parser.add_argument("--install", metavar="PATH", help="copy skills into PATH/.claude/skills/")
    args = parser.parse_args()

    dirs = skill_dirs()
    failed = False
    for d in dirs:
        errors = validate_skill(d)
        status = "ok" if not errors else "FAIL"
        print("%-24s %s" % (d.name, status))
        for err in errors:
            print("    - " + err)
        failed = failed or bool(errors)
    if failed:
        sys.exit("\nValidation failed.")
    print("\n%d skills valid." % len(dirs))

    if args.check:
        return
    if args.install:
        for d in dirs:
            print("installed  " + str(install(d, args.install)))
        return
    for d in dirs:
        print("built      " + str(build_zip(d).relative_to(ROOT)))
    print("built      " + str(build_plugin_zip(dirs).relative_to(ROOT)))


if __name__ == "__main__":
    main()
