"""Regenerate every figure: each module in lecture_figures.figures with a make()."""

import importlib
import pkgutil
import sys

from lecture_figures import figures, style


def main() -> None:
    style.apply_style()
    only = set(sys.argv[1:])
    for module_info in pkgutil.iter_modules(figures.__path__):
        if only and module_info.name not in only:
            continue
        module = importlib.import_module(f"{figures.__name__}.{module_info.name}")
        if hasattr(module, "make"):
            print(f"Making {module_info.name}")
            module.make()


if __name__ == "__main__":
    main()
