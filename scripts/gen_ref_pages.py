"""Generate the code reference pages."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

root = Path(__file__).parent.parent
src = root / "sparse/numba_backend/_coo"
#breakpoint()
for path in sorted(src.rglob("*.py")):
    module_path = path.relative_to(root).with_suffix("")
    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = Path("api", doc_path)

    parts = tuple(module_path.parts)
    #breakpoint()
    #if parts[-1] == "__init__":
    #    parts = parts[:-1]
    #    continue
    #    doc_path = doc_path.with_name("index.md")
    #    full_doc_path = full_doc_path.with_name("index.md")
    #elif parts[-1] == "__main__":
    #    continue
    ##breakpoint()
    #nav[parts] = doc_path.as_posix()

    if parts[-1] == "common" or parts[-1] == "core":
        nav[parts] = doc_path.as_posix()
        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            identifier = ".".join(parts)
            print("::: " + identifier, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path.relative_to(root))

with mkdocs_gen_files.open("api/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
