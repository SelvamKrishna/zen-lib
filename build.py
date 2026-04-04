import os
import sys
import shutil
import subprocess

BUILD_DIRECTORY = "build"
BUILD_GENERATOR = "Unix Makefiles"
BUILD_TYPE = "Release"

TEST_DIRECTORY = "./_test"
TEST_SOURCE = f"{TEST_DIRECTORY}/main.cpp"

LIB_NAME = "zenlib"


def run_cmd(cmd: list[str], fail_desc: str = "", fail_fix_steps: list[str] = []) -> None:
    print("\033[0;34m$ >\033[0m", " ".join(cmd))

    try:
        subprocess.run(cmd, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print(f"\033[0;33m{fail_desc}\033[0m")
        for i, step in enumerate(fail_fix_steps):
            print(f"  \033[0;30m{i}.\033[0m {step}")
        print("\n")
        sys.exit(0)


def main() -> None:
    test_flag = "test" in sys.argv

    run_cmd(
        ["cmake", "--version"], "Cmake not found", [
            "Install CMake: https://cmake.org/download/",
            "Configure build options within this file",
            "Run this script from the project root",
            "[optional] Add 'clean' command to create a clean build",
        ]
    )

    if "clean" in sys.argv and os.path.exists(BUILD_DIRECTORY):
        print("\033[0;32mCleaning build directory...\033[0m")
        shutil.rmtree(BUILD_DIRECTORY)

    run_cmd(
        [
            "cmake", "-S", ".",
            "-B", BUILD_DIRECTORY, "-G", BUILD_GENERATOR,
            f"-DCMAKE_BUILD_TYPE={"Debug" if test_flag else BUILD_TYPE}"
        ], "Invalid build config provided", [
            "Ensure BUILD_DIRECTORY is valid",
            "Ensure BUILD_GENERATOR is valid",
            "Ensure BUILD_TYPE is [Debug, Release, RelWithDebInfo, MinSizeRel]",
        ]
    )

    run_cmd(["cmake", "--build", BUILD_DIRECTORY, "--parallel"])

    # --- (Dev-Only) VVV ---

    if test_flag:
        print("\033[0;32m[dev] Testing...\033[0m")

        TEST_OUTPUT = f"{BUILD_DIRECTORY}/testout"

        run_cmd([
            "g++", TEST_SOURCE, "-std=c++23", "-I.", f"-L{BUILD_DIRECTORY}", f"-l{LIB_NAME}",
            "-g", "-O0", "-Wall", "-Wextra", "-Wpedantic", "-Werror",
            "-o", TEST_OUTPUT
        ])

        run_cmd([f"./{TEST_OUTPUT}"])


if __name__ == "__main__":
    main()
