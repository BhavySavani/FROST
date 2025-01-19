module spi#(parameter clk_frequency)
(
    input clk,
    input miso,
    output mosi,
    output sclk,
    output cs
);
reg [3:0] count;

initial begin
    count = 0;
end

always @(posedge clk) begin
    count = count + 1;
    if (count == 10) begin
        count = 0;
    end
end
endmodule