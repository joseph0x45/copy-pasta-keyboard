cmake_minimum_required(VERSION 3.30)
include(pico_sdk_import.cmake)

set(PICO_BOARD pico_w)

project(blink C CXX ASM)

pico_sdk_init()

# This version should behave exactly the same, but it runs the sys clock slowly.
add_executable(main
  main.c
)
target_link_libraries(main
  pico_stdlib              # for core functionality
  pico_cyw43_arch_none     # we need Wifi to access the GPIO, but we don't need anything else
  hardware_clocks
)
# This requires us to modify the pio divisor to successfully communicate with the cyw43 chip
target_compile_definitions(
  main PRIVATE
  CYW43_PIO_CLOCK_DIV_DYNAMIC=1
)

# create map/bin/hex file etc.
pico_add_extra_outputs(main)
