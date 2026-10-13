#!/usr/bin/env python3
"""chaizhao skill 规范校验器。

校验两层约束：
1. agentskills.io 开放规范（frontmatter 必填项、命名规则、长度上限、引用完整性）
2. 本仓库自身纪律（SKILL.md 不得引用案例素材路径）

用法：python3 scripts/validate.py   （exit 0 = 通过，exit 1 = 有违规）
"""
import re
import sys
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"
MAX_DESCRIPTION = 1024
MAX_SKILL_LINES = 500
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# 本仓库纪律：案例素材不得进入 skill（用户要求：方法论而非案例库）
FORBIDDEN_IN_SKILL = ["拆解示例/", "examples/", "demo-analysis"]


def check_skill(skill_dir: pathlib.Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir}: 缺少 SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        return [f"{skill_dir.name}: SKILL.md 缺少 frontmatter"]
    front = fm.group(1)

    # name：必填、与目录名一致、字符集合规
    name = re.search(r"^name:\s*(\S+)\s*$", front, re.M)
    if not name:
        errors.append(f"{skill_dir.name}: frontmatter 缺 name")
    else:
        n = name.group(1)
        if n != skill_dir.name:
            errors.append(f"{skill_dir.name}: name '{n}' 与目录名不一致")
        if not NAME_RE.fullmatch(n):
            errors.append(f"{skill_dir.name}: name '{n}' 违反字符集（小写字母/数字/连字符，不连-不首尾-）")

    # description：必填、≤1024 字符
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    if not desc:
        errors.append(f"{skill_dir.name}: frontmatter 缺 description")
    else:
        dlen = len(desc.group(1))
        if dlen > MAX_DESCRIPTION:
            errors.append(f"{skill_dir.name}: description {dlen} 字符，超上限 {MAX_DESCRIPTION}")

    # 行数上限
    n_lines = text.count("\n") + 1
    if n_lines > MAX_SKILL_LINES:
        errors.append(f"{skill_dir.name}: SKILL.md {n_lines} 行，超上限 {MAX_SKILL_LINES}")

    # 引用完整性：references/ 一级相对引用必须存在
    for ref in sorted(set(re.findall(r"references/[A-Za-z0-9_\-]+\.md", text))):
        if not (skill_dir / ref).exists():
            errors.append(f"{skill_dir.name}: 引用的文件不存在: {ref}")

    # 本仓库纪律：案例素材路径泄漏
    for bad in FORBIDDEN_IN_SKILL:
        if bad in text:
            errors.append(f"{skill_dir.name}: SKILL.md 引用了案例素材（'{bad}'）——方法论不进案例")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"未找到 skills/ 目录: {SKILLS_DIR}")
        return 1
    all_errors: list[str] = []
    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        all_errors.extend(check_skill(skill_dir))

    if all_errors:
        print("✗ 校验未通过：")
        for e in all_errors:
            print(f"  - {e}")
        return 1
    print("✓ 规范校验通过（frontmatter / 命名 / 长度 / 引用完整性 / 无案例泄漏）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
