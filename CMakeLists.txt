cmake_minimum_required(VERSION 3.25)

project(zen VERSION 0.1.0 LANGUAGES CXX)

include(FetchContent)

FetchContent_Declare(
    zen-math
    GIT_REPOSITORY https://github.com/SelvamKrishna/zen-math.git
    GIT_TAG main
)

FetchContent_MakeAvailable(zen-math)

add_library(zen INTERFACE)

target_link_libraries(zen
    INTERFACE
    zen::math
)
