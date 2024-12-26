#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"
#include "pico/cyw43_driver.h"
#include "hardware/clocks.h"

int main() {
    set_sys_clock_khz(18000, true);
    cyw43_set_pio_clock_divisor(1, 0);

    stdio_init_all();
    if (cyw43_arch_init()) {
        printf("Wi-Fi init failed");
        return -1;
    }
    while (true) {
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
        sleep_ms(250);
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
        sleep_ms(250);
    }
}
