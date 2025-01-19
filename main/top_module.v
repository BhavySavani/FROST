module top_module (
input wire sensor1_uart_clk,
input wire sensor1_uart_rx,
input wire sensor2_uart_clk,
input wire sensor2_uart_rx,
input wire sensor3_spi_clk,
input wire sensor3_spi_miso,
output wire sensor1_uart_tx,
output wire sensor1_uart_tx_out,
output wire sensor2_uart_tx,
output wire sensor2_uart_tx_out,
output wire sensor3_spi_mosi,
output wire sensor3_spi_cs,
output wire sensor3_spi_sckl
);

    uart sensor1_uart#(
    .baud_rate(9600),
    .clk_frequency(50000000)
) (
    .clk(sensor1_uart_clk),
    .rx(sensor1_uart_rx),
    .tx(sensor1_uart_tx),
    .tx_out(sensor1_uart_tx_out)
    );

    uart sensor2_uart#(
    .baud_rate(115200),
    .clk_frequency(50000000)
) (
    .clk(sensor2_uart_clk),
    .rx(sensor2_uart_rx),
    .tx(sensor2_uart_tx),
    .tx_out(sensor2_uart_tx_out)
    );

    spi sensor3_spi (
    .clk(sensor3_spi_clk),
    .miso(sensor3_spi_miso),
    .mosi(sensor3_spi_mosi),
    .cs(sensor3_spi_cs),
    .sckl(sensor3_spi_sckl)
    );

endmodule
