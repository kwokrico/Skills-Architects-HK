import json
import sys

from hk_architect_skills.dispatcher import HKSkillsDispatcher


def dispatch(tool_name, arguments=None):
    return HKSkillsDispatcher().dispatch(tool_name, arguments or {})


def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input:
            return

        input_data = json.loads(raw_input)
        tool_name = input_data.get("tool")
        arguments = input_data.get("arguments", {})
        result = dispatch(tool_name, arguments)
        sys.stdout.write(json.dumps(result))

    except Exception as e:
        sys.stdout.write(json.dumps({"error": f"Dispatcher Error: {str(e)}"}))


if __name__ == "__main__":
    main()
