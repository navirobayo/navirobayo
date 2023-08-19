// Quick excercise using the conditional Switch-Case.  
// Enjoy cowboy. 

function saltarLinea() {
    document.write("<br>");
}

function imprimir(frase) {
    document.write(frase);
    saltarLinea();
}

var edad = parseInt(prompt("¿Cuál es tu edad?"));
var tieneLicencia = prompt("¿Tienes licencia? Responde S o N");

if (edad >= 18) {
    switch(tieneLicencia){
        case "S":
            imprimir("Estas listo vaquero. Bienvenido al club");
            break;
        case "s":
            imprimir("Estas listo vaquero. Bienvenido al club");
            break;
        case "N":
            imprimir("Consigue tu licencia adicto a la velocidad!");
            break;
        case "n":
            imprimir("Consigue tu licencia adicto a la velocidad!");
            break;
        default: 
            imprimir("wtf");
    }
}

if (edad < 18) {
    switch(tieneLicencia){
        case "S":
            imprimir("Eso es increíble bebé vaquero");
            break;
        case "s":
            imprimir("Eso es increíble bebé vaquero");
            break;
        case "N":
            imprimir("¿Qué pretendes bebé vaquero?");
            break;
        case "n":
            imprimir("¿Qué pretendes bebé vaquero?");
            break;
        default: 
            imprimir("wtf");
    }
}
