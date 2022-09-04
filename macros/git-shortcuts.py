from adafruit_hid.keycode import Keycode

app = {                       # REQUIRED dict, must be named 'app'
    'name': 'Git Shortcuts',  # Application name
    'macros': [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x5D00A2, 'pull', ['git pull\n']),
        (0x74008B, 'push', ['git push\n']),
        (0xff006d, 'commit', ['git commit -m "']),
        # 2nd row ----------
        (0xff000d, 'add', ['git add .\n']),
        (0xFF5D00, 'stash', ['git stash']),
        (0xFF8B00, 'unstash', ['git stash apply']),
        # 3rd row ----------
        (0xffeb3b, 'commit', ['git commit -m ']),
        (0xafe313, 'status', ['git status\n']),
        (0x00ff00, 'diff', ['git diff\n']),

        # 4th row ----------
        (0x00fa9a, 'branch', ['git checkout -b ']),
        (0x2372b3, 'clean', ['git reset HEAD --hard']),
        (0x0000FF, '', []),

        # Encoder button ---
        (0xFFF, '', [])
    ]
}
