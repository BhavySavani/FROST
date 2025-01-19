module RS485 #(clk_frequency)
(
    input clk,
    input rx,
    output tx
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
