void main() {
  print("Vas a ejecutar tu método en 3, 2, 1");
  int ejemplo1 = 2;
  int ejemplo2 = 3;
  int resultado = miMetodo(miNumero1: ejemplo1, miNumero2: ejemplo2);
  print(resultado);
  int resultadoAdicional = miMetodo(miNumero1: ejemplo1, miNumero2: resultado);
  print(resultadoAdicional);
  print("Ejecutaste tu primer método");
}

int miMetodo({required int miNumero1, required int miNumero2}) {
  int resultadoMiMetodo = miNumero1 + miNumero2;
  return resultadoMiMetodo;
}
