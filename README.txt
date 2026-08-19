1. ¿Qué sucede si intentas descifrar con una llave diferente a la que se usó para cifrar? 

Básicamente el programa igual "descifra" algo, pero sale puro chino — bytes random sin sentido. Como el unpad espera encontrar un relleno específico al final del texto, casi siempre explota con un error tipo ValueError. O sea, sin la llave correcta no hay forma de recuperar el mensaje original, ni por casualidad.

2. ¿Por qué el IV debe ser diferente cada vez que ciframos, aunque usemos la misma llave? 

Porque si no, dos mensajes que empiecen igual (cifrados con la misma llave) van a dar el mismo primer bloque cifrado, y ahí un atacante ya puede empezar a sacar conclusiones aunque no tenga la llave. El IV lo que hace es "revolver" el cifrado desde el principio para que cada vez salga distinto, aunque el texto y la llave sean los mismos. Si usara siempre el mismo IV, estaría filtrando patrones sin darme cuenta.

3.  ¿Cuál es la relación entre el tamaño de la llave y la seguridad del cifrado? ¿Cuántas 
combinaciones posibles tiene una llave de 256 bits? 

Mientras más grande la llave, más combinaciones tiene que probar alguien si quiere adivinarla a la fuerza. Con 256 combinaciones, que es un número gigante. O sea, ni con todos los computadores del mundo juntos alguien la va a poder reventar por fuerza bruta en un tiempo razonable.

4. ¿Por qué se necesita padding? ¿Qué tamaño tiene un bloque AES y qué pasa si el texto 
plano no es múltiplo de ese tamaño? 

AES trabaja en bloques fijos de 16 bytes, no le puedes pasar cualquier cantidad de texto. Entonces si tu mensaje no calza justo en múltiplos de 16, hay que rellenar lo que falta con bytes extra para completar el bloque. Eso es el padding. Al descifrar, se sabe exactamente cuánto relleno quitar porque el mismo relleno indica cuántos bytes son.

5. ¿Por qué se utiliza base64 para almacenar el resultado? ¿Cuál es la diferencia entre guardar 
bytes crudos y base64? 

Porque el cyphertext y el IV son puros bytes crudos, y muchos de esos bytes no son caracteres normales. Base64 los transforma en puro texto (letras, números y algunos símbolos) para que se puedan guardar o mandar sin drama. Eso sí, el archivo queda un poco más pesado que si guardaras los bytes asi solo.

6.¿Cómo se relaciona este cifrado simétrico con el problema del doble gasto y la confianza 
que analizaste en la dinámica de compraventa? 

El cifrado simétrico protege que nadie lea la comunicación entre dos partes, pero no evita que alguien intente gastar la misma plata digital dos veces. Eso se resuelve con otra cosa: el consenso de la red y las firmas digitales, que usan criptografía asimétrica. O sea, el cifrado simétrico te da privacidad en la conversación, pero la confianza de que la transacción es válida y única viene de otro lado.