
from operator import indexOf
import random

def showdiff(dict_now, dict_next):
    import io
    import sys

    def colorIfDifferent(val, old):
        # Red color terminal escape if different (for interactive terminals)
        return f'\033[91m{val}\033[0m' if val != old else str(val)

    def dict_ascii(dict_now, dict_prev=None):
        """
        Terminal art: render the dictionary as a vertical crazy "list",
        with ASCII decorations, colors (for changes), arrows for changed items,
        and a little "busyness" around value changes.
        """
        dict_prev = dict_prev or {}
        keys = sorted(set(dict_now.keys()) | set(dict_prev.keys()))
        if not keys:
            print("┏━━━━━━━━━━━━┓")
            print("┃  (empty)   ┃")
            print("┗━━━━━━━━━━━━┛")
            return

        # For nice alignment
        keylen = max(len(str(k)) for k in keys)
        vallen_now = max(len(str(dict_now.get(k, ""))) for k in keys)
        vallen_prev = max(len(str(dict_prev.get(k, ""))) for k in keys)
        vallen = max(vallen_now, vallen_prev)
        box_min = 18
        boxwidth = max(keylen + vallen + 13, box_min)  # Wider for the art

        # Art chars
        top = " ⎧" + "═"* (boxwidth - 4) + "⎫ "
        bot = " ⎩" + "═"* (boxwidth - 4) + "⎭ "
        print(top)
        print("  ∴ DICTIONARY LIST ∴".center(boxwidth))
        print(" " + "·"* (boxwidth - 2))
        for idx, k in enumerate(keys):
            val_now = dict_now.get(k, "")
            val_prev = dict_prev.get(k, None)
            # Compose line art per item
            changed = (val_now != val_prev)
            key_str = f"{k}".ljust(keylen)
            val_disp = colorIfDifferent(val_now, val_prev) if dict_prev else str(val_now)
            arrow = ""
            left_bracket = "⟦"
            right_bracket = "⟧"
            # Crazy list: an ASCII "node"
            node = "-" if idx % 2 == 0 else "✶"
            # If changed, arrow and noise
            if dict_prev and changed:
                arrow = " ⇒"
                node = "✹"
                val_boxed = f"\033[5m⟦{val_disp}⟧\033[0m"  # flashing box (maybe)
            else:
                val_boxed = f"{left_bracket}{val_disp}{right_bracket}"
            line = f"  {node} {key_str} : {val_boxed: <{vallen+4}}{arrow}"
            if changed and dict_prev:
                line += " \033[91m~ changed ~\033[0m"
            print(line)
        print(" " + "·"* (boxwidth - 2))
        print(bot)

    def capture_ascii(f, *args, **kwargs):
        buf = io.StringIO()
        oldout = sys.stdout
        sys.stdout = buf
        try:
            f(*args, **kwargs)
        finally:
            sys.stdout = oldout
        return buf.getvalue().splitlines()

    before_lines = capture_ascii(dict_ascii, dict_now)
    after_lines = capture_ascii(dict_ascii, dict_next, dict_now)
    width = max(len(line) for line in before_lines) if before_lines else 0
    max_lines = max(len(before_lines), len(after_lines))
    print("[Before]".ljust(width + 6) + "[After]")
    for i in range(max_lines):
        l = before_lines[i] if i < len(before_lines) else ""
        r = after_lines[i] if i < len(after_lines) else ""
        print(l.ljust(width + 6) + r)
    print()


def dictprinter(func):
    def wrapper(dictionary, *args, **kwargs):
        if not isinstance(dictionary, dict):
            raise TypeError("First argument must be a dict")
        copy = dictionary.copy()
        print(f"Calling: {func.__name__}({', '.join(['dictionary']+ [repr(a) for a in args] + [f'{k}={v!r}' for k, v in kwargs.items()])})")
        rslt = func(dictionary, *args, **kwargs)
        showdiff(copy, rslt)
        return rslt
    return wrapper

@dictprinter
def add_mountain(dictionary, name, height):
    dictionary[name] = height
    return dictionary

@dictprinter
def change_height(dictionary, name, new_height):
    if name in dictionary:
        dictionary[name] = new_height
    return dictionary

def get_highest_mountain(dictionary):
    if not dictionary:
        return None
    max_key = max(dictionary, key=dictionary.get)
    return {max_key: dictionary[max_key]}

# Example usage
mountains_dict = {}
mountain_names = ["Alps", "Andes", "Rockies", "Himalayas", "Ural", "Atlas", "Carpathians", "Sierra"]
for j in range(4):
    for i, name in enumerate(mountain_names):
        mountain_h = random.randint(1, 200)
        if name in mountains_dict:
            change_height(mountains_dict, name, j)
        else:
            add_mountain(mountains_dict, name, mountain_h)


# End of script – nothing to keep open for ASCII out