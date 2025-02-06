module i2c#(parameter addr, clk_frequency)
(
    inout sda,
    output scl,
    input clk
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