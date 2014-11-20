// Esta ula possui capacidade de trabalhar com operandos negativos,
// portanto são destinados 1 bit pro sinal e 31 bits para dados.
// Dessa forma, a ALU do nosso processador possui a capacidade de
// trabalhar com dados de -2147483648 até +2147483648.
module alu(
	input signed [31:0] op1,
	input signed [31:0] op2,
	input [2:0] func,
	
	output reg signed [31:0] result,
	output reg overflow,
	output reg equals,
	output reg above,
	output reg zero
);

// Inicializa as saídas, de forma que todas estejam zeradas até que
// sejam modificadas pelo algoritmo da ALU
initial begin
	zero = 1'b0;
	above = 1'b0;
	equals = 1'b0;
	overflow = 1'b0;
	result = 32'b00000000000000000000000000000000;
end

// Sempre que uma função for designada para este bloco, será avaliado
// o que foi recebido, para assim, processar a requisição.
always @ (func) begin

	// Analiza a função recebida a aplica o cálculo requisitado
	case(func)
		3'b000: result = op1 + op2;
		3'b001: result = op1 - op2;
		3'b010: result = op1 * op2;
		3'b011: result = op1 / op2;
		3'b100: result = op1 & op2;
		3'b101: result = op1 | op2;
		3'b110: result = !op1;
	endcase

	// Após executar a requisição é necessário avaliar e modificar,
	// caso necessário, os valores de saída registrados em cada flag
	if (func == 3'b001 && result > 0) begin
		above = 1'b1;
	end else
		if (func == 3'b001 && result == 0) begin
			equals = 1'b1;
	end else
		if ( (func == 3'b000 || func == 3'b001 || func == 3'b010)
		&& (result < -2147483648 || result > 2147483648) ) begin
			overflow = 1'b1;
	end  else
		if (func == 3'b011 || op2 == 0) begin
			overflow = 1'b1;
	end
end

endmodule