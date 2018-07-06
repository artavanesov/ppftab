# Surpy

import random

surpy = random.randint(1, 5)

if surpy == 1:
    print("""
        "When you arise in the morning, think of what a precious privilege
        it is to be alive - to breathe, to think, to enjoy, to love."
        - Marcus Aurelius
        """)
elif surpy == 2:
    print(
        """
        "Immature love says: 'I love you because I need you.'
        Mature love says: 'I need you because I love you.'"
        - Erich Fromm
        """
    )
elif surpy == 3:
    print(
        """
        "Do not fear difficulty. Hard ground makes stronger roots."
        - Ventari
        """
    )
elif surpy == 4:
    print(
        """
        "Lesser, greater, middling, it's all the same. Proportions are negotiated,
        boundaries blurred. I'm not a pious hermit, I haven't done only good in my life.
        But if I'm to choose between one evil and another, then I prefer not to choose at all.""
        - Geralt of Rivia
        """
    )
elif surpy == 5:
    print(
        """
        “Who controls the past controls the future. Who controls the present controls the past.”
        ― George Orwell
        """
    )
else:
    print("Something went wrong.")

input("\n\nPress the Enter key to exit.")
