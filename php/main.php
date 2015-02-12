<?php

    // Se usa una tabla de traduccion
    $desde = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    $a     = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM";
    
    // La funcion strtr de php traduce, utilizando ambas secuencias
    $s = trim(fgets(STDIN));
    echo sprintf("Escribiste: %s\n", $s);
    $rot13 = strtr($s, $desde, $a);
    echo sprintf("rot13: %s\n", $rot13);
?>
