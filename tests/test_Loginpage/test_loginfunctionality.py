from logging import log
import re
from playwright.sync_api import Page, expect


def test_loginfunctionality(page):
    page.goto("https://www.google.com/?zx=1763794504740&no_sw_cr=1")
    log.info("Navigated to Google homepage")
    page.get_by_role("combobox", name="Search").click()
    log.info("Clicked on the search combobox")
    page.get_by_role("combobox", name="Search").fill("Microsoft")
    log.info("Filled 'Microsoft' in the search combobox")
    expect(page.get_by_text("About this page")).to_be_visible()
    log.info("Verified that 'About this page' text is visible on the page")


import logging
from pathlib import Path
from datetime import datetime
BASE_LOG_DIR = Path("logs")
BASE_LOG_DIR.mkdir(exist_ok=True)

logger = None
def configure_logger_for_test(test_name: str):
    """Configure logger dynamically based on test function name."""
    global logger

    # Create daily folder
    today_folder = BASE_LOG_DIR / datetime.now().strftime("%Y-%m-%d")
    today_folder.mkdir(exist_ok=True)

    # Dynamic file name: test function HH-MM-SS.log
    timestamp = datetime.now().strftime("%H-%M-%S")
    log_file = today_folder / f"{test_name}_{timestamp}.log"

    # Create logger for this test
    dynamic_logger = logging.getLogger(test_name)
    dynamic_logger.setLevel(logging.INFO)
    dynamic_logger.propagate = False

    # Add console handler if not present
    if not any(isinstance(h, logging.StreamHandler) for h in dynamic_logger.handlers):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        dynamic_logger.addHandler(console_handler)

    # Add file handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
    dynamic_logger.addHandler(file_handler)

    # Capture execution start
    exec_start = datetime.now()
    exec_start_str = exec_start.strftime("%Y-%m-%d %H:%M:%S Central Time (US & Canada)")

    # Write EXECUTION_BEGIN at top
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"EXECUTION_BEGIN: {exec_start_str}\n")

    # Update global alias
    logger = dynamic_logger

    print(f"✔️ Logs for '{test_name}' will be saved in: {log_file}")

    return log_file, exec_start

import logging
from pathlib import Path
from datetime import datetime
BASE_LOG_DIR = Path("logs")
BASE_LOG_DIR.mkdir(exist_ok=True)

logger = None
def configure_logger_for_test(test_name: str):
    """Configure logger dynamically based on test function name."""
    global logger

    # Create daily folder
    today_folder = BASE_LOG_DIR / datetime.now().strftime("%Y-%m-%d")
    today_folder.mkdir(exist_ok=True)

    # Dynamic file name: test function HH-MM-SS.log
    timestamp = datetime.now().strftime("%H-%M-%S")
    log_file = today_folder / f"{test_name}_{timestamp}.log"

    # Create logger for this test
    dynamic_logger = logging.getLogger(test_name)
    dynamic_logger.setLevel(logging.INFO)
    dynamic_logger.propagate = False

    # Add console handler if not present
    if not any(isinstance(h, logging.StreamHandler) for h in dynamic_logger.handlers):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        dynamic_logger.addHandler(console_handler)

    # Add file handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
    dynamic_logger.addHandler(file_handler)

    # Capture execution start
    exec_start = datetime.now()
    exec_start_str = exec_start.strftime("%Y-%m-%d %H:%M:%S Central Time (US & Canada)")

    # Write EXECUTION_BEGIN at top
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"EXECUTION_BEGIN: {exec_start_str}\n")

    # Update global alias
    logger = dynamic_logger

    print(f"✔️ Logs for '{test_name}' will be saved in: {log_file}")

    return log_file, exec_start


def finalize_test_log(log_file: Path, exec_start: datetime):
    """Add EXECUTION_END and duration at top only."""
    exec_end = datetime.now()
    exec_end_str = exec_end.strftime("%m-%d-%Y %H:%M:%S Central Time (US & Canada)")
    duration = exec_end - exec_start
    with open(log_file, "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.write(f"EXECUTION_BEGIN: {exec_start.strftime('%m-%d-%Y %H:%M:%S Central Time (US & Canada)')}\n")
        f.write(f"EXECUTION_END: {exec_end_str}\n")
        f.write(f"EXECUTION_DURATION: {duration}\n\n")
        f.write(content)