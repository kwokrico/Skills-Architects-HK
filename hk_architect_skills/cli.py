"""CLI entry for Claude Desktop stdin JSON dispatch (skills tools only)."""

import json
import sys

from hk_architect_skills.dispatcher import HKSkillsDispatcher


def main():
    try:
        raw = sys.stdin.read()
        if not raw:
            return
        payload = json.loads(raw)
        dispatcher = HKSkillsDispatcher()
        result = dispatcher.dispatch(payload.get("tool"), payload.get("arguments", {}))
        sys.stdout.write(json.dumps(result))
    except Exception as exc:
        sys.stdout.write(json.dumps({"error": f"Dispatcher Error: {exc}"}))


if __name__ == "__main__":
    main()
