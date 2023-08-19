<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF=8">
        <title>Encriptador Ver 1.1 </title>
        <link rel="stylesheet" href="reset.css">
        <link rel="stylesheet" href="style_encript1.css">
    </head>
    <body>
        <br>
        <h1>Sprint 01: Encriptador Alura</h1><br>
        <h2>"From Colombia with love."</h2><br><br><br>
        <main>
            <textarea id="mensaje" rows="5" autofocus required>Bienvenido programador. Ingresa el mensaje a cifrar o descifrar. </textarea>

            <button class="button1" onclick="encript()">Encriptar mensaje</button>

            <button class="button2" onclick="desencript()">Desencriptar mensaje</button>

            

        </main>
        <script>
            var mensaje1 = document.getElementById("mensaje"); 

            function encript() {
                var coded = (mensaje1.value.replace(/e/g, "enter").replace(/i/g, "imes").replace(/a/g, "ai").replace(/o/g, "ober").replace(/u/g, "ufat"))
                
                document.getElementById("mensaje").value= coded
            }

            function desencript() {
                var decoded = (mensaje1.value.replace(/enter/g, "e").replace(/imes/g, "i").replace(/ai/g, "a").replace(/ober/g, "o").replace(/ufat/g, "u")) 

                document.getElementById("mensaje").value= decoded
            }
        </script>
        <footer>
            <p>Solución para el programa de formación de Alura junto a Oracle Next Education: ONE. </p><br> <p> Escrito y diseñado por Ivan Robayo. GitHub: <a target="_blank" rel="noopener noreferrer" href="https://github.com/jhonnyvector"> @jhonnyvector</a> LinkedIn: <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/soyivan1997/">/soyivan1997</a> Twitter: <a target="_blank" rel="noopener noreferrer" href="https://twitter.com/vector_jhonny">@vector_jhonny</a></p><br>
        </footer>
    </body>
</html>
