# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/98_Convert_raw_image_to_jpg.ipynb (unless otherwise specified).

__all__ = ['get_suffixes', 'convert_files_with_darktable']

# Cell


from pathlib import Path
from typing import Tuple, Optional, Dict, List, Union, Callable, Iterable, Set

# Internal Cell


from fastcore.script import *
import numpy as np
from shutil import copy
import os
import random
import time
import progressbar
from progressbar import FormatLabel

# Internal Cell


def glob_suffixes(root_path: Path, suffixes: Union[List[str], str]) -> List[Path]:
    if isinstance(suffixes, str):
        suffixes = [suffixes]
    return sorted([f for f in root_path.glob("**/*") if file_suffix_in(f, suffixes)])

# Cell


@call_parse
def get_suffixes(
    path: Param("input directory containing images", Path),
    verbose: Param("", bool) = True,
) -> Set[str]:
    """Returns all unique suffixes"""
    path = Path(path)
    p = path.glob("**/*")
    files = [x.suffix for x in p if x.is_file()]
    if verbose:
        print(list(set(x.lower() for x in files)))
    return set(x.lower() for x in files)

# Internal Cell


def get_rand_file_with_suff(
    path: Path, suffix: str, case_insensitive: bool = True
) -> Path:
    """Returns a random file that has a suffix equal to the variable suff"""
    if case_insensitive:
        p = [p for p in path.glob(f"**/*") if p.suffix.lower() == suffix.lower()]
    else:
        p = path.glob(f"**/*{suffix}")
    files = [x for x in p if x.is_file()]
    return random.choice(files)

# Internal Cell


def get_one_image_for_each_suffix(path: Path) -> List[Path]:
    """Returns one random image for each suffix"""
    return [
        get_rand_file_with_suff(path, suffix)
        for suffix in get_suffixes(path, verbose=False)
    ]

# Internal Cell


def create_sample_test_dir_if_needed(
    dst: Path = Path("../../data/testing/raw"),
) -> List[Path]:
    """Creates samples for a test set"""
    dst.mkdir(parents=True, exist_ok=True)
    if len(list(dst.glob("*"))) == 0:
        files = get_one_image_for_each_suffix(dropbox_path)
        for f in files:
            copy(f, dst)
    return list(dst.glob("*"))

# Internal Cell


def convert_image_to_jpg_darktable(
    img_path: Path,
    *,
    suffixes_to_delete: List[str] = [".mov", ".mp4"],
    remove_src: bool = False,
    update_msg_fn: Callable[[str], None] = print,
) -> str:
    update_msg_fn(f"Processing {img_path}")
    """Converts image whose suffix is not in the skip_suffixes list, if remove_src = True then deletes the input image"""
    if img_path.suffix.lower() != ".jpg":
        dst = img_path.parent / (img_path.stem + ".jpg")
        if img_path.suffix.lower() in suffixes_to_delete:
            if remove_src:
                retmsg = f"Removed {img_path} because {img_path.suffix.lower()} is in {suffixes_to_delete}"
                img_path.unlink()
            else:
                retmsg = f"Not removing {img_path} although {img_path.suffix.lower()} is in {suffixes_to_delete}"
            return None, retmsg
        if dst.exists() and remove_src:
            img_path.unlink()
            retmsg = f"Removed {img_path} because {dst} exists."
            return dst, retmsg
        system_error = os.system(f"darktable-cli {img_path} {dst}")
        if system_error != 0:
            retmsg = f"Converted error {system_error}, image path {img_path}."
            return img_path, retmsg
        if remove_src:
            img_path.unlink()
        retmsg = f"Converted {img_path} to {dst}."
        return dst, retmsg
    else:
        retmsg = f"Skiped path {img_path} because it is already a JPEG."
        return img_path, retmsg

# Cell


@call_parse
def convert_files_with_darktable(
    root_path: Param("input directory containing images to convert", Path),
    remove_src: Param("input True if you want to delete the images ", bool) = True,
):
    """Calls the convert_image_to_jpg() function on all images in the path"""
    root_path = Path(root_path)
    widgets = [
        FormatLabel(""),
        " [",
        progressbar.Timer(),
        "] ",
        progressbar.Bar(),
        progressbar.Percentage("%(percentage)5.2f%%"),
        " (",
        progressbar.AdaptiveETA(),
        ") ",
    ]
    files = sorted([x for x in root_path.glob("**/*") if x.is_file()])
    n_files = len(files)

    def update_msg(msg):
        widgets[0] = FormatLabel(f"[{i:4d}/{n_files}] {msg}")

    log = []
    with progressbar.ProgressBar(max_value=len(files), widgets=widgets) as bar:
        for i, src in enumerate(files):
            _, msg = convert_image_to_jpg_darktable(
                src, remove_src=remove_src, update_msg_fn=update_msg
            )
            log.append(msg)
            bar.update(i)
    print(f"Conversion completed {len(files)}/{len(files)}")

    for msg in log:
        print(msg)