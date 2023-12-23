set(SOURCES
    algorithms.cpp
    tests.cpp
)

add_library(lib STATIC ${SOURCES})

target_include_directories(lib PUBLIC "./")