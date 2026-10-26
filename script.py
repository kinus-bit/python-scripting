"""
QUICK REFERENCE: running vs importing a Python file
====================================================

THE BIG IDEA
------------
A Python file can be used in two ways:
  1. RUN directly from the terminal  ->  python script.py
  2. IMPORTED by another file/notebook ->  import script

The line `if __name__ == '__main__':` lets the file know which way it is
being used, so it only does the "run" part when you actually run it.


PART 1: INSIDE script.py  (no.1)
--------------------------------
    def name():
        print("This guy is Kinuthia the scripting guru")

    if __name__ == '__main__':
        name()

  * `def name():`
        Puts the print inside a function, so it is reusable and can be
        called as many times as you want.

  * `__name__`
        A built-in variable that every Python file has.
          - File run directly (python script.py)  -> __name__ == '__main__'
          - File imported (import script)         -> __name__ == 'script'
                                                     (the file's own name)

  * `if __name__ == '__main__':`
        Means "only run the indented code if this file is being run
        directly". When the file is imported, this is False, so name()
        does NOT run automatically.

  Terminal result:
      (py) C:\\Users\\kinus\\Downloads\\pythonscripting> python script.py
      This guy is Kinuthia the scripting guru
      (`(py)` is just the active virtual environment.)


PART 2: INSIDE THE JUPYTER NOTEBOOK  (no.2)
-------------------------------------------
    import script
    script.name()

  * `import script`
        Loads script.py as a module. The file must be in the same folder
        as the notebook (or on Python's path). Nothing prints here,
        because the `__main__` guard is False. The function is only
        defined, not called.

  * `script.name()`
        You call the function yourself using  module.function()  syntax.
        THIS is the moment the message prints.


WHY IT WAS DONE THIS WAY
------------------------
  * Reuse the same code from the terminal AND the notebook, no copy-paste.
  * No surprise output on import; you decide when name() runs.
  * One file works both as a script and as a module.


HANDY VARIATIONS
----------------
    from script import name        # import just the function
    name()                         # no `script.` prefix needed

    import script as s             # give the module a short alias
    s.name()


JUPYTER GOTCHA
--------------
If you edit script.py after importing it, the notebook keeps using the OLD
version. Fix it by restarting the kernel, or reloading:

    import importlib
    importlib.reload(script)


SUMMARY TABLE
-------------
    How the file is used    | __name__ value | Does name() auto-run?
    ------------------------|----------------|----------------------
    python script.py        | '__main__'     | YES
    import script           | 'script'       | NO (call it yourself)
"""


def name():
    print("This guy is Kinuthia the scripting guru")


# no.1
if __name__ == '__main__':
    name()

# no.2
import script
script.name()

# no.1 is for the one written inside the script.py file
# no.2 is for the one written inside the jupyter notebook